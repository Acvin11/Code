#include <iostream>
#include <stdexcept>
#include <cstdio>

using namespace std;

string runUnixCommandAndCaptureOutput(string cmd) {
   char buffer[128];
   string result = "";
   FILE* pipe = popen(cmd.c_str(), "r");
   if (!pipe) throw std::runtime_error("popen() failed!");
   try {
      while (!feof(pipe)) {
         if (fgets(buffer, 128, pipe) != NULL)
            result += buffer;
      }
   } catch (...) {
      pclose(pipe);
      throw;
   }
   pclose(pipe);
   return result;
}

int main() {
   string cmd = "ls -lh";
   cout << runUnixCommandAndCaptureOutput(cmd) << endl;
   return 0;
}