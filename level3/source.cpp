#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

pair<int, int> level1(const string &);
void modify(vector<vector<char>> &, int, int, const string &, pair<int, int>);
bool validate(const vector<vector<char>> &);
void verify(const vector<vector<char>> &);
void verify(const vector<vector<char>> &);

int main() {
  string file = "level3_example";
  ifstream file_in;
  ofstream file_out;

  file_in.open(file + ".in");
  file_out.open(file + ".out");

  if(file_in.is_open()) {
    int n;
    file_in >> n;

    for(int i = 0; i < n; i++) {
      int c, l;
      file_in >> c;
      file_in >> l;
      
      vector<vector<char>> garden;
      
      for(int j = 0; j < l; j++) {
        vector<char> x;
        string line;
        file_in >> line;

        for(auto c : line)
          x.push_back(c);
        garden.push_back(x);
      }
      string lawn;
      file_in >> lawn;
      pair<int, int> start = level1(lawn);
      modify(garden, c, l, lawn, start);
      verify(garden);

      if(validate(garden)) file_out << "VALID" << endl;
      else file_out << "INVALID" << endl;
    }
    file_in.close();
    file_out.close();
  }
  return 0;
}

pair<int, int> level1(const string &s) {
  pair<int, int> res;
  int minX = 0;
  int minY = 0;

  int x = 0;
  int y = 0;

  for(char c : s){
    switch(c) {
      case 'W':
        y -= 1;
        minY = min(minY, y);
        break;
      
      case 'S':
        y += 1;
        break;
      
      case 'A':
        x -= 1;
        minX = min(minX, x);
        break;

      case 'D':
        x += 1;
        break;
      
      default:
        break;
    }
  }

  res.first = abs(minY);
  res.second = abs(minX);
  return res;
}

void modify(vector<vector<char>> &garden, int c, int l, const string &lawn, pair<int, int> start) {
  int i = start.first;
  int j = start.second;

  for(char c : lawn) {
    if(i < l && j < c && garden[i][j] == '.')
      garden[i][j] = 'Y';
    else break;

    switch(c) {
      case 'W':
        i -= 1;
        break;
      
      case 'S':
        i += 1;
        break;
      
      case 'A':
        j -= 1;
        break;

      case 'D':
        j += 1;
        break;
      
      default:
        break;
    }
  }
  if(i < l && j < c && garden[i][j] == '.')
    garden[i][j] = 'Y';
}

bool validate(const vector<vector<char>> &garden) {
  for(auto a : garden) {
    for(auto b : a) {
      if(b == '.') return false;
    } 
  }
  return true;
}

void verify(const vector<vector<char>> &garden) {
  for(auto a : garden) {
    for(auto b : a)
      cout << b;
    cout << endl;
  }
  cout << endl;
}