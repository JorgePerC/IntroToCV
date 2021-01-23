# IntroToCV
Files to learn CV, for the moment, only in Python.

So... I'm really new to this.

*Remember* to activate your venv

## Topics I should learn: 

- [x] Python, objects
- [x] Python, list comprenhension
- [x] Python, Generators
- [] Whats a mask
- [] Whats a kernel
- [] Color spaces
- [] Convolutions
- [] Filters
- [] Leonardo Chang
- [] Sistemas embebidos (C++)

### Math:

- [] Even more matrix
- [] Used funcitons (Canny, Gaussian blur etc. )

## Bibliography

Someone recommended me this site to learn on my own: https://www.pyimagesearch.com/

Also, I'll be guiding my-self on this book:
https://0-eds-a-ebscohost-com.biblioteca-ils.tec.mx/eds/detail/detail?vid=0&sid=54d403c0-3c57-4154-b93e-40080aea1644%40sdc-v-sessmgr01&bdata=Jmxhbmc9ZXMmc2l0ZT1lZHMtbGl2ZSZzY29wZT1zaXRl#AN=1403105&db=e000xww

This book seems interesting: 
https://0-eds-a-ebscohost-com.biblioteca-ils.tec.mx/eds/detail/detail?vid=0&sid=77841371-eab4-42e5-a09b-87faefad9ab5%40sessionmgr4006&bdata=Jmxhbmc9ZXMmc2l0ZT1lZHMtbGl2ZSZzY29wZT1zaXRl#AN=1809133&db=e000xww

*You shouuld use a **Tec account** to read them

### Links that have helped me:

* How to prepare Jetson (TRUE PAIN IN THE ASS): https://www.pyimagesearch.com/2020/03/25/how-to-configure-your-nvidia-jetson-nano-for-computer-vision-and-deep-learning/

* How to use VIM: https://coderwall.com/p/adv71w/basic-vim-commands-for-getting-started

* Vimtutor (comand)

* What is a VEM: https://realpython.com/python-virtual-environments-a-primer/

* Program to get camera pipeline: https://github.com/JetsonHacksNano/CSI-Camera

* Numpy: https://forums.developer.nvidia.com/t/scipy-not-getting-installed-on-jetson-nano-inspite-of-all-dependencies/110034

* YT video: https://www.youtube.com/watch?v=WQeoO7MI0Bs

* Standford playlist: https://youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv

## What I learned from *vimtutor*:

The following are based on the default setting. Maybe I can change them later.

1. To move the cursor:
    * h <-
    * l ->
    * k R
    * j v
    *I can also use arrows, but its supossed to be slower. 

2. Exit Vim:
    * Press <ESC> to enter *nomal mode*. In order for the following commands to work, you should be on normal mode. 
    * To save:   :wq  + <ENTER>
    * To not save:  :q!  + <ENTER>


3. Modify file:
    * x -> Delete character on cursor
    * i -> Insert character (left) of cursor.
        * Here you can't use hjkl to move. You should go into *normal mode*.
        * You can use arrows to move. 
        * You can't delete anything previous of what you just wrote. Except for supr.
    * A -> "Append". This is just like insert but the difference relies on the fact that you'll be overiding characters as you go by, instead of simply adding them. Hmmmmm... Thats how it worked for me, but the description says something different. 
    * dw -> Delete word. 
        * If you are not on the word's first character, then it's going to delete from the character that you were untill the end.  
        * If you keep w pressed, then you'll jump between words. 
        * There are more commands to delete. *d* is the deafult letter for this action. Hoever, I see it as uncesary to learn the rest of the commands. 
    * dd -> Delete line. 
    * d$ -> Delete the rest of the line from where your cursor is. 
    * **.** -> Delete line. 
        * If at the end, it starts going backguards. 


4. Open files:
    * Open bash.
    * Go to the desired folder.
    * ´vim *fileName*´