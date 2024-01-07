# Pomodoro app
- This project maily focuses on introducing us with the concept of canvas widget in the tkinter library
- Other than that this project helps to understand more about how to work with tkinter

## Canvas Widget
- It works similar to a canvas i.e., using this we put things on top of each other.
- Configuring items of canvas like image and text is a bit different
- Let say if we are configuring timer_text we need to do 
  - `canvas.itemconfig(timer_text, text="")`

## Previous Knowledge used 
- buttons 
- labels
- grid layout etc.

## Setting up the timer 
- Creating the timer was a bit challenging, to solve this we were introduced to after method.
- The logic used for setting the timer was:
  - `window.after(1000, count_down, count - 1)`
  - this executes the passed function i.e., `count_down()` after 1000ms.
  - also we used recursion to achieve the count-down mechanism.

## Resetting the timer
- Finally, the last part of the program was to set up the reset functionality this was achieved by:
  - `window.after_cancel(timer)` the timer var had `window.after(1000, count_down, count - 1)`
- In the `reset_timer()` we also had to reset all the parameter as they were initially.