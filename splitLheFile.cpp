// g++ -Wall -o splitLheFile splitLheFile.cpp

#include <iostream>
#include <fstream>
#include <cstdlib>

int main(int argc, char** argv)
{
  if(argc != 5)
  {
    std::cout << ">>>splitLheFile.cpp::Usage:   " << argv[0] << "   inFile.lhe   #eventsToSkip   #eventsToCopy out.lhe" << std::endl;
    return -1;
  }
  
  char* inFileName = argv[1]; 
  int eventsToSkip = atoi(argv[2]);
  int eventsToCopy = atoi(argv[3]);
  char* outFileName = argv[4]; 

  std::cout << "inFileName = " << inFileName << std::endl;
  std::cout << "eventsToSkip = " << eventsToSkip << std::endl;
  std::cout << "eventsToCopy = " << eventsToCopy << std::endl;
  std::cout << "outFileName = " << outFileName << std::endl;
  
  
  
  // open lhe file
  std::ifstream inFile(inFileName, std::ios::in);
  std::ofstream outFile(outFileName, std::ios::out);
  
  std::string line;
  bool skipEvent = false;
  int eventIt = 0;
  
  while(!inFile.eof())
  {
    getline(inFile, line);
    
    
    // decide whether to skip event or not 
    if( line == "<event>" )
    {
      ++eventIt;
      if( eventIt <= eventsToSkip )
        skipEvent = true;
      if( eventIt > eventsToSkip+eventsToCopy )
        skipEvent = true;
    }
    
    
    // write line to outFile
    if(skipEvent == false)
      outFile << line << std::endl;
    
    
    // end of event
    if( line == "</event>" )
      skipEvent = false;
  }
  
  
  return 0;
}

