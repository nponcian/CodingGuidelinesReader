CodingGuidelinesReader

Purpose\
Since not everyone would make an effort on an everyday basis to continuously read and refresh knowledge about C++ coding guidelines, this particular shell script repository will aid and help to solve that problem. As long as users login everyday to their respective GNU/Linux machines be it at work or at home, this script can be setup to automatically display the C++ coding guidelines without any explicit request from the user (more information about this in Step 4::Item 3.a.2. below). And the good thing about it is that the user will not be overwhelmed by hundreds to thousands of lines of guidelines which reading all at once might only lead to forgetting it the next day, because this script controls how many guidelines will show up for the day. Treat it as something like "Your C++ coding guideline tips for the day".

Requirements


Usage

Step 1:
cd ./Path/To/Where/You/Will/Put/The/CodingGuidelinesReader

Step 2:
git clone https://github.com/nponcian/CodingGuidelinesReader.git

Step 3:
chmod a+rwx ./Path/To/CodingGuidelinesReader/ConfigFiles
- This is only necessary if a single copy of this CodingGuidelinesReader repository is intended to be used by different users on a shared common device, as this will make the ConfigFiles directory within this CodingGuidelinesReader repository to be readable, writable, and executable by anyone.

Step 4:
Different ways to execute (regardless of what directory you are currently in):
1. As a binary
    1. Invoke by doing any of the following
        1. invoke through relative path <../Path/To/CodingGuidelinesReader/showcppguide>
        2. invoke through absolute path </Path/To/CodingGuidelinesReader/showcppguide>
        3. invoke through relative path with flags <../Path/To/CodingGuidelinesReader/showcppguide --help>
        4. invoke through absolute path with flags </Path/To/CodingGuidelinesReader/showcppguide --help>
2. As a shell script
    1. Invoke by doing any of the following
        1. invoke through relative path <bash ../Path/To/CodingGuidelinesReader/showcppguide>
        2. invoke through absolute path <bash /Path/To/CodingGuidelinesReader/showcppguide>
        3. invoke through relative path with flags <bash ../Path/To/CodingGuidelinesReader/showcppguide --help>
        4. invoke through absolute path with flags <bash /Path/To/CodingGuidelinesReader/showcppguide --help>
3. As a shell script that is to be included into current shell instance
    1. Source the script either on current working directory or on \~/.bashrc file
        1. Source the script on current working directory
            1. invoke source or . through relative path <source ../Path/To/CodingGuidelinesReader/showcppguide --moduleabsolutepath /Path/To/CodingGuidelinesReader>
            2. invoke source or . through absolute path <source /Path/To/CodingGuidelinesReader/showcppguide --moduleabsolutepath /Path/To/CodingGuidelinesReader>
        2. Source the script on \~/.bashrc file
            1. edit <vim ~/.bashrc>
            2. add line that will source or . through absolute path <source /Path/To/CodingGuidelinesReader/showcppguide --moduleabsolutepath /Path/To/CodingGuidelinesReader>
    2. Invoke by doing any of the following
        1. invoke through the sourced function <showcppguide>
        2. invoke through the sourced function with flags <showcppguide --help>
    3. Some notes
        1. As long as you have sourced the script correctly with flag --moduleabsolutepath, then the invoke could be done wherever directory you are currently in even if different from the original directory to where source command was issued
        2. The option of adding the source command into \~/.bashrc file would make the script to automatically run and be available upon login to shell without explicit user request

Step 5:
Execute with flag --help to see the list of other available flags
