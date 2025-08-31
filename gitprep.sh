#!/bin/bash
git add .
echo "Enter your commit message: "
read msg
git commit -m "$msg"
