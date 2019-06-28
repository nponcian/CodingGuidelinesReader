CodingGuidelinesReader

## PURPOSE
Since not everyone would make an effort on an everyday basis to continuously read and refresh knowledge about C++ coding guidelines, this particular shell script repository will aid and help to solve that problem. As long as users login everyday to their respective GNU/Linux machines be it at work or at home, this script can be setup to automatically display the C++ coding guidelines without any explicit request from the user (more information about this in Usage::4::3 below). And the good thing about it is that the user will not be overwhelmed by hundreds to thousands of lines of guidelines which reading all at once might only lead to forgetting it the next day, because this script controls how many guidelines will show up for the day. Treat it as something like "Your C++ coding guideline tips for the day".

## REQUIREMENTS
1. GNU/Linux environment
    * Either:
        1. Full operating system
        2. Virtual machine (as a guest OS)
        3. Cygwin
        3. etc.
2. Git (optional if you just prefer to do a download and extract from GitHub)
    ~~~
    sudo apt install git
    ~~~

## USAGE
1. Clone (or download and extract) the repository
~~~
git clone https://github.com/nponcian/CodingGuidelinesReader.git
~~~

2. Go to the repository
~~~
cd CodingGuidelinesReader
~~~

3. Change the access rights of ConfigFiles directory
~~~
chmod a+rwx ConfigFiles/
~~~
* This is only necessary if a single copy of this CodingGuidelinesReader repository is intended to be used by different users on a shared common device, as this will make the ConfigFiles directory within this CodingGuidelinesReader repository to be readable, writable, and executable by anyone that will write their own config files to it.

4. Different ways to execute (regardless of what directory you are currently in):
    1. As a binary
        1. Invoke by doing any of the following
            1. invoke through relative path *../Path/To/CodingGuidelinesReader/showcppguide*
            2. invoke through absolute path */Path/To/CodingGuidelinesReader/showcppguide*
            3. invoke through relative path with flags *../Path/To/CodingGuidelinesReader/showcppguide --help*
            4. invoke through absolute path with flags */Path/To/CodingGuidelinesReader/showcppguide --help*
    2. As a shell script
        1. Invoke by doing any of the following
            1. invoke through relative path *bash ../Path/To/CodingGuidelinesReader/showcppguide*
            2. invoke through absolute path *bash /Path/To/CodingGuidelinesReader/showcppguide*
            3. invoke through relative path with flags *bash ../Path/To/CodingGuidelinesReader/showcppguide --help*
            4. invoke through absolute path with flags *bash /Path/To/CodingGuidelinesReader/showcppguide --help*
    3. As a shell script that is to be sourced into the current shell instance
        1. Source the script either on current working directory or on \~/.bashrc file
            1. Source the script on current working directory
                1. invoke source or . through absolute path *source /Path/To/CodingGuidelinesReader/showcppguide*
            2. Source the script on \~/.bashrc file
                1. edit *vim ~/.bashrc*
                2. add line that will source or . through absolute path *source /Path/To/CodingGuidelinesReader/showcppguide*
        2. Invoke by doing any of the following
            1. invoke through the sourced function *showcppguide*
            2. invoke through the sourced function with flags *showcppguide --help*
        3. Some notes
            1. As long as you have sourced the script correctly with the complete absolute path, then the invoke could be done wherever directory you are currently in even if different from the original directory to where source command was issued
            2. The option of adding the source command into \~/.bashrc file would make the script to automatically run and be available upon login to shell without explicit user request

5. Execute with flag *--help* to see the list of other available flags
