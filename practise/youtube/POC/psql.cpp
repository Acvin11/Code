// g++ mysql_service.cpp ; ./a.out

#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif
#include <iostream>
#include <cstdlib>
#include <bits/stdc++.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <dirent.h>
// #include "Utility.h"
#include <iostream>
#include <cstring>
#ifdef _WIN32
#include <Shlobj.h>
#endif

using namespace std;
#define MAX_BUFF 1024
#define OPERATION_RC_SUCCESS 0
#define OPERATION_RC_FAILURE 1
#define PGSTART 1
#define PGSTOP 0
#define CONF_FILE "postgresql.conf"
#define RECOVERY_SIGNAL_FILE "recovery.signal"
#define tar_extension ".tar"

#include <string>
#include <functional>
#include <dirent.h>

// g++ mysql_service.cpp ; ./a.out

#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif
#include <iostream>
#include <cstdlib>
#include <bits/stdc++.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <dirent.h>
// #include "Utility.h"
#include <iostream>
#include <cstring>
#ifdef _WIN32
#include <Shlobj.h>
#endif

using namespace std;
#define MAX_BUFF 1024
#define OPERATION_RC_SUCCESS 0
#define OPERATION_RC_FAILURE 1
#define PGSTART 1
#define PGSTOP 0
#define CONF_FILE "postgresql.conf"
#define RECOVERY_SIGNAL_FILE "recovery.signal"
#define tar_extension ".tar"

#define RECOVERY_COMMAND 0
#define ARCHIEVE_COMMAND 1
#define STSTEMCTL_ENV_COMMAND 2

void findAndReplaceAll(std::string &data, std::string toSearch, std::string replaceStr)
{
    size_t pos = data.find(toSearch);
    while (pos != std::string::npos)
    {
        data.replace(pos, toSearch.size(), replaceStr);
        pos = data.find(toSearch, pos + replaceStr.size());
    }
}

int writeConfFile(string version, std::string dataDirPath, std::string archieveDirPath, int strReplaceChoice)
{
     cout << "\n Inside writeConfFile " << dataDirPath << std::endl;
     cout << "Inside archieveDirPath " << archieveDirPath << std::endl;
     
    int status = OPERATION_RC_SUCCESS;
    ostringstream text;
    string filePath;
    std::string archievePath = archieveDirPath;
#ifndef _WIN32 
    
    if (strReplaceChoice == 0 || strReplaceChoice == 1)
    {
        filePath = dataDirPath + "/" +CONF_FILE;
    }
    else
    {
        // filePath = dataDirPath + "postgresql-" + version + ".service"; //just for checking sake
        filePath = "/usr/lib/systemd/system/postgresql-" + version + ".service"; // actual path
    }
    std::string dummyPath = dataDirPath + "/dump_" + CONF_FILE;

#else
    findAndReplaceAll(archievePath, "\\", "\\\\");
    if (strReplaceChoice == 0 || strReplaceChoice == 1)
    {
        filePath = dataDirPath + "\\" + CONF_FILE;
    }
    std::string dummyPath = dataDirPath + "\\dump_" + CONF_FILE;
#endif

    cout << "FilePath : " << filePath << "|" << std::endl;

    fstream inFile2 (filePath.c_str());
    string line, dataItem;

    ofstream out(dummyPath.c_str());
    while( getline(inFile2, line) )
    {    
        stringstream ls( line );
        string word;
        size_t pos;
        if (strReplaceChoice == 0)
            pos = line.find("restore_command");
        else if (strReplaceChoice == 1)
            pos = line.find("archive_command");
        else
            pos = line.find("Environment=PGDATA=");

        // cout << "before line : " << line << "|" << std::endl;
        if (pos != string::npos)
        { 
            inFile2.clear();
            // cout << "\n pos : " << pos << "|" << std::endl;
            std::string strReplace;
            int lineLen = line.length();
            std::string newDataLine = line.substr( pos, line.length());
            
#ifdef _WIN32
            if (strReplaceChoice == 0)
            {
                strReplace = "restore_command = \'copy \"" + archievePath + "%f\" \"%p\"\'"; //  new archieveDirPath path
            }
            else if (strReplaceChoice == 1)
            {
                /// archive_command = 'copy "%p" "C:\\server\\archivedir\\%f"'
                strReplace = "archive_command = \'copy \"%p\" \"" + archievePath + "%f\"\'"; //  new archieveDirPath path
            }
#else
            if (strReplaceChoice == 0)
            {
                strReplace = "restore_command = \'cp \"" + archievePath + "%f\" %p\'"; //  new archieveDirPath path
            }
            else if (strReplaceChoice == 1)
            {
                //archive_command = 'test ! -f /mnt/server/archivedir/%f && cp %p /mnt/server/archivedir/%f'  # Unix
                strReplace = "archive_command = \'test ! -f \"" + archievePath + "%f\" && cp %p \"" + archievePath + "%f\"\'"; //  new archieveDirPath path
            }
            else
            {
                strReplace = "Environment=PGDATA=" + dataDirPath; // new datadirectory path
            }
#endif	
            // findAndReplaceAll(line, "#", "");
            // findAndReplaceAll(line, newDataLine, strReplace);
            strReplace += " # ";
            cout << "updated line : " << line << "|" << std::endl;
            cout << "updated newDataLine : " << newDataLine << "|" << std::endl;
            cout << "updated strReplace : " << strReplace << "|" << std::endl;
            line = strReplace;
            
            
        }
        text << line;
        text << "\n";
    }
    string data = text.str();
    if (data.empty())
    {
        cout << "data empty : " <<  "|" << std::endl;
        return OPERATION_RC_FAILURE;
    }
    out << data;
    inFile2.close();
    out.close();
    remove(filePath.c_str());

    cout << "\nfilePath : " << filePath << "|" << std::endl;
    cout << "dummyPath : " << dummyPath << "|" << std::endl;
    cout << "data : " << data.size() << "|" << std::endl;

    if (rename(dummyPath.c_str(), filePath.c_str()) != 0)
        perror("Error moving file");
    else
        cout << "File moved successfully";
    return OPERATION_RC_SUCCESS;
}


int main()
{
    int result = OPERATION_RC_SUCCESS;
    bool isInstallerMethod = true;
    cout << "intiated isInstallerMethod : " << isInstallerMethod << std::endl;
    string postgresOperation;
    string user = "postgres";
    string creds = "Gyp.s8m";
    string restoreFilePath;
    std::string scheduleType;

#ifndef _WIN32
    string dataDirectory = "/root/mainline/restore";
    string targetDir = "/root/mainline/data";
    string port = "5432";
    string version = "14";
    // restoreFilePath = "/root/mainline/full/non_stream_compress";
    // restoreFilePath = "/root/mainline/full/non_stream_non_compress";
    // restoreFilePath = "/root/mainline/full/stream_compress";
    // restoreFilePath = "/root/mainline/full/stream_non_compress";

    restoreFilePath = "/myStorage/";
    // restoreFilePath = "/root/mainline/incr/stream/";

#else
    string dataDirectory = "C:\\mainline2\\dumpDir\\";
    string targetDir = "C:\\mainline2\\data\\";
    string port = "5432";
    string version = "14";
    restoreFilePath = "C:\\mainline\\lvm";
    // string dataDirPath = "C:\\mainline\\dumpDir";  //to be changed
#endif

    // non stream_compression  full:
    //   tar -C "C:\server\archivedir" -xvf "C:\mainline\218_restoredata\pgbase_backup\with_compression\non_stream_full\pgarchive\simple\pg_wal.tar.gz"

    //   tar -C "C:\Program Files\PostgreSQL\14\data" -xvf "C:\mainline\218_restoredata\pgbase_backup\with_compression\non_stream_full\pgarchive\simple\base.tar.gz"
   //type nul > "C:\Program Files\PostgreSQL\14\data\recovery.signal"
    std::string dataDirPath ="C:\\Program Files\\PostgreSQL\\14\\data";
    std::string archieveDirPath ="C:\\server\\archivedir\\";
    
    // string command = "tar -C \"C:\\Program Files\\PostgreSQL\\14\\data\" -xvf \"C:\\mainline\\218_restoredata\\pgbase_backup\\with_compression\\non_stream_full\\pgarchive\\simple\\base.tar.gz\"";
    //string command = "tar -C \"C:\\Program Files\\PostgreSQL\\14\\data\" -xvf \"C:\\mainline\\218_restoredata\\pgbase_backup\\with_compression\\non_stream_incr\\pgarchive\\simple\\base.tar.gz\"";
    string command = "xcopy \"C:\\mainline\\218_restoredata\\lvm\\incr\\pgarchive\" \"C:\\server\\archivedir\" /c /i /e /h /y  ";
    result = system(command.c_str());
    std::cout << "base : " << result << endl;
    if (result != OPERATION_RC_SUCCESS)
    {
        return OPERATION_RC_FAILURE;
    }

    // string command2 = "tar -C \"C:\\server\\archivedir\" -xvf \"C:\\mainline\\218_restoredata\\pgbase_backup\\with_compression\\non_stream_full\\pgarchive\\simple\\pg_wal.tar.gz\"";
    //string command2 = "tar -C \"C:\\server\\archivedir\" -xvf \"C:\\mainline\\218_restoredata\\pgbase_backup\\with_compression\\non_stream_incr\\pgarchive\\simple\\pg_wal.tar.gz\"";
   string command2 = "xcopy \"C:\\mainline\\218_restoredata\\lvm\\incr\" \"C:\\Program Files\\PostgreSQL\\14\\data\" /c /i /e /h /y  ";
    result = system(command2.c_str());
    std::cout << "pg_wal : " << result << endl;
    if (result != OPERATION_RC_SUCCESS)
    {
        return OPERATION_RC_FAILURE;
    }

    string command3 = "type nul > \"C:\\Program Files\\PostgreSQL\\14\\data\\recovery.signal\"";
    result = system(command3.c_str());
    std::cout << "touch file : " << result << endl;
    if (result != OPERATION_RC_SUCCESS)
    {
        return OPERATION_RC_FAILURE;
    }

    string command4 = "attrib -S  -r \"" + dataDirPath + "\\*.*\" /S /D";
    result = system(command4.c_str());
    std::cout << "data dir file : " << result << endl;
    if (result != OPERATION_RC_SUCCESS)
    {
        return OPERATION_RC_FAILURE;
    }

    string command5 = "attrib -S  -r \"" + archieveDirPath + "\\*.*\" /S /D";
    result = system(command5.c_str());
    std::cout << "archieveDirPath file : " << result << endl;
    if (result != OPERATION_RC_SUCCESS)
    {
        return OPERATION_RC_FAILURE;
    }

    result = writeConfFile(version, dataDirPath, archieveDirPath, RECOVERY_COMMAND);
    std::cout << "RECOVERY_COMMAND writeConfFile : " << result << endl;
    if (result != OPERATION_RC_SUCCESS)
    {
        return OPERATION_RC_FAILURE;
    }

    std::cout << " result : " << result << endl;
    return result;
}

// Command: set PGPASSWORD=Gyp.s8m&& psql -h localhost -p 5432 -U postgres -t -A -c "show data_directory;" > output.txt
