# FilesCollect-Py

### STATUS
Development. v0.04. Remaining tasks are...
- develop tor/onion features to completion: 1) is everything present that needs to be. 2) possibly requires login period after pressing b to begin start, with progress display, ie "Connecting To Onion.."? 
- progress during download of file: 1) list all filtered files, 2) one by one display "Downloading: examplefilename.pdf", "Completed: examplefilename". 3) final summary stats, completed, failed. 
- format menu 100% correctly. 
- check everything over.
- run live tests & bugfix.
- Finish documentation.

## DESCRIPTION
FilesCollect is an advanced web scraping utility designed to streamline the process of collecting files from websites while prioritizing user privacy and convenience. It features an interactive menu that allows users to specify the target URL and file types they wish to download. Leveraging the Tor/Onion network through the Torpy library, FilesCollect offers an enhanced privacy mode for anonymous operations. It ensures a seamless user experience by persistently storing settings in a settings.json file and organizes downloaded files into directories mirroring the URL's structure. With its capability to handle standard and Tor-based web sessions, FilesCollect stands out as a robust and user-friendly tool for efficient web scraping and file management.

### FEATURES
- **Interactive Menu**: Streamlined navigation through a user-friendly interface, enabling URL input and file type specification.
- **Enhanced Privacy**: Utilizes the Tor/Onion network via the Torpy library, offering **anonymous & free**, VPN-based downloads.
- **Persistent Settings**: Seamlessly retains user preferences, including the base URL and file types, across sessions using a `settings.json` file.
- **Scraping and Downloading**: Efficiently extracts and retrieves specified file types from web pages, maintaining a well-organized download structure.
- **Container Extraction**: Employs a unique directory system based on the webpage's URL, ensuring structured storage and easy access to **collected files**.
- **Adaptive Error Handling**: Intelligently manages runtime errors and network issues, ensuring uninterrupted operation and robust performance.

### PREVIEW
- Early version (needs updating when its bugfixed)...
```

=======================( FilesCollect )======================




                      1. Page Location.
                               ()                               

                       2. File Extension.
                              (None)

                       3. Toggle Privacy
                         (Standard Mode)




Select :- Menu Options = 1-3, Begin Rip = B, Exit Menu = X:

```

## USAGE
1. Run `Setup-Install.Bat`, and then, check the libraries all installs correctly and run again as required.
2. Run `FilesCollect-Py.Bat`, and then configure using options 1-3.
3. Press `b` to begin, then watch as the scripts, optionally connect to tor and download the specified files from the specified location.
4. Examine summary screen, determine if all the files were correctly downloaded.
5. Check the `.\Downloads` folder for your files, and then move them to your intended location.    

### REQUIREMENTS
Install is not easy, this will be written further later..
1. Python stuff...
```
pip install requests
pip install beautifulsoup4
pip install torpy
pip install requests[socks]
```
2. Tor Service
```
Download the Tor Expert Bundle: https://www.torproject.org/download/tor/
Extract the Bundle, Run the Tor Service
```
3. Run the program...
```
run FilesCollect-Py.Bat
```


### NOTATION
- A creator, releases his work for free, you try to click through them selectively, but, there are too many and they are each in multiple formats, you, want them all and dont want it in all formats.
- After you digest multiple downloads, you notice FilesCollect-Py saved most of the url as the folder name, which included the, author and project name, you know, where to go and who, to donate. 

## DISCLAIMER
This software is subject to the terms in License.Txt, covering usage, distribution, and modifications. For full details on your rights and obligations, refer to License.Txt.
