# Toast Alert

Do you hate it when you put something in the toaster, but your zoomer attention span means you get distracted in less than a minute? Tell me about it. 

That's why I created this! The most useful Discord bot know to mankind. 

All you need is a Raspberry Pi or any other micro computer able to run python, a Pi Pico or any other microcontroller with an ADC and a toaster that you can tear apart without shocking yourself and you're good to go!

## What does it do?

Well, currently working together my Pico and Zero check the voltage on a toaster's electro magnet, and when it goes on it logs that so when it goes back down it knows the toast is done.
From there it finds any one of my friends from 3 select servers and tells them to tell me that my toast is ready. So useful!

## How to use it? 

![lol](https://c.tenor.com/UCBnVC7FlvUAAAAC/tenor.gif)

Well, maybe you do, you're probably smarter than I am.

All I did was flash the pico script onto the... pico, and then set the bot script to run on boot from a bash script. 

A virtual environment for python was needed, at least for me it was the easiest way to get things running. This is my fist attempt at doing anything with microcontrollers, Raspberry Pis and Python. 
