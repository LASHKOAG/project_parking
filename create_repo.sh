#!/bin/bash

git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/LASHKOAG/project_parking.git
git push -u origin main