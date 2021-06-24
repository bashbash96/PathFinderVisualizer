
# Shortest Path Finder Visualizer

> A simple visualizer that simulates the shortest path Algorithms.

<div align="center">
  <img src="https://drive.google.com/uc?export=view&id=1Tg-y9gsyxpT8CNrsPxfm7wVDP2dfOl8u" width="400" height="300"/>
  <img src="https://drive.google.com/uc?export=view&id=1nuLw57JuaOkNvMQlgM4lx6-935hjRmn_" width="400" height="300"/>
</div>

<br>

---

### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Description

Program that simulates the steps of three different Algorithms for finding shortest path:
  1. BFS
  2. A* with Manhattan distance.
  3. A* with Euclidean distance.

The program allows controls over:
  1. The size of the screen.
  2. Number of rows in this screen.
  3. The speed of each step of the Algorithms.


Strategy **Desing Pattern** was used to allow ***SOLID*** principles while using more one algorithm to solve the same problem. 

Colors in the grid:
  - Orange - start point.  
  - Blue - end point. 
  - Black - barrier. 
  - White - empty cell.
  - Green - visited cell but not its neighbors.
  - Red - visited cell and its neighbors.
  - Purple - cell is part of the shortest path.


### Technologies

- Python
- Pycharm
- Pygame
- Tkinter

[Back To The Top](#shortest-path-finder-visualizer)

---

## How To Use

Instructions:
  1. Run main.py
  2. Insert the size of the screen (800 recommended).
  3. Insert the grid rows (20 recommended).
  4. Insert the speed of the algorithms steps (50 recommended), the bigger the slower.
  5. Add points using the mouse left button:  
     - Add start point (Orange).  
     - Add end point (Blue).  
     - Add barriers (Black).  
  6. Remove points using the mouse right button.
  7. Run one of the algorithms:  
     - Click 1 to run BFS.  
     - Click 2 to run A* with Manhattan distance.  
     - Click 3 to run A* with Euclidean distance
  8. Click C to clean the grid.


### Installation

- Copy this link ***https://github.com/bashbash96/google-auto-complete-text.git*** then on cmd or bash do:

		cd ~/Desktop
		git clone {{the link you just copied}} auto-complete

- This creates a directory named "Project", clones the repository there and adds a remote named "origin" back to the source.

		cd auto-complete
		git checkout develop

- If that last command fails

		git checkout -b develop

------------
### Updating/The Development Cycle

You now have a git repository, likely with two branches: main and develop. Now bake these laws into your mind and process:

You will never commit to ***main*** or ***develop*** directly .

Instead, you will create ***feature branches*** on your machine that exist for the purpose of solving singular issues. You will always base your features off the develop branch.

		git checkout develop
		git checkout -b my-feature-branch

This last command creates a new branch named "my-feature-branch" based off of develop. You can name that branch whatever you like. You should not have to push it to Github unless you intend to work on multiple machines on that feature.

Make changes.

	git add .
	git commit -am "I have made some changes."

This adds any new files to be tracked and makes a commit. Now let's add them to develop.

	git checkout develop
	git merge --no-ff my-feature-branch
	git push origin develop
------------
### Releasing

Finished with your project?

- Create a feature branch as normal.
- Update the version history in the README.md file
- Update this to develop as normal.

		git checkout master
		git merge --no-ff develop
		git push origin master
		git tag v1.0.0
		git push origin v1.0.0
------------

### Back-end

To run locally, do the following on Backend directory:

1. Create a Python 3.5 virtualenv

2. Install dependencies:
	
```
pip install -r requirements/dev.txt
npm install
```

   Alternatively, use the make task:

```
make install
```
    

you can run:

```
python main.py
```
then follow the instructions in [Instructions Section](#how-to-use)


[Back To The Top](#shortest-path-finder-visualizer)


---

## References

[`Python`](https://www.python.org/)
[`Pycharm`](https://www.jetbrains.com/pycharm/)

[Back To The Top](#shortest-path-finder-visualizer)

---
## License

GPL License

Copyright (c) [2020] [Amjad Bashiti]

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

[Back To The Top](#shortest-path-finder-visualizer)

---
## Author Info

- Github - [bashbash96](https://github.com/bashbash96) 
- Linkedin - [amjad-bashiti](https://www.linkedin.com/in/amjad-bashiti-2652a9192/)



[Back To The Top](#shortest-path-finder-visualizer)
