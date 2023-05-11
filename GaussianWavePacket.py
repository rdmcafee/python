# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 11:03:09 2021

@author: Mcrye
"""

" simulate waves on a string
" Program to accompany "Computational Physics" by N. Giordano and H. Nakanishi
" Copyright Prentice Hall 1997, 2006
"
" modified by H. Nakanishi for i/o and boundary conditions
"
program waves
   option NOLET
   dim x(0 to 1000,3)
   call init(x,dt,dx,c,nmax,bc,n1,store$,sigma,x0,x1)
   if store$ <> "" then
      open #2: name store$, organization text, create newold
      erase #2
      set #2: ZONEWIDTH 12
      print #2, using "+#.#####^^^^": 0;
      set #2: ZONEWIDTH 3
      print #2: ", ";
      set #2: ZONEWIDTH 12
      print #2, using "+#.#####^^^^": x(n1,2)
   end if
   red$="red"
   black$="black"
   white$="white"
   clear
   set cursor 1,10
   print "Propagation Gaussian Wave in one dimension"
   set cursor 2,10
   print "peak of width =";sigma;" located at x =";x0;
   if store$ <> "" then print ", recorded at x =";x1
   print
   set cursor 3,10
   print "dx ="; dx; ", dt ="; dt; ", c ="; c;", boundary =";bc
   set cursor 5,10
   print "Hit any key to pause, q or x to quit"
   open #1: screen 0.1,0.9,0.1,0.9
   set window -2*dx,(nmax+2)*dx,-1.5,1.5
   call axes(x,dx,nmax)
   call display(x,dx,nmax,red$,0,dt)
   i = 0
   do
      call display(x,dx,nmax,white$,i,dt)
      call propagate(x,dt,dx,c,nmax,bc,n1)
      i = i+1
      if store$ <> "" then
         set #2: ZONEWIDTH 12
         print #2, using "+#.#####^^^^": i*dt;
         set #2: ZONEWIDTH 3
         print #2: ", ";
         set #2: ZONEWIDTH 12
         print #2, using "+#.#####^^^^": x(n1,2)
      end if
      call display(x,dx,nmax,red$,i,dt)
      if key input then 
         get key z
         if chr$(z) = "q" or chr$(z) = "x" then
            exit do
         else
            get key z
            if chr$(z) = "q" or chr$(z) = "x" then exit do
         end if
      end if
   loop
   if store$ <> "" then close #2
   close #1
end

!   y(,) is a two dimensional array containing the displacement at
!      the current time step y(i,2), the previous time step y(i,1)
!      the next time step corresponds to y(i,3)
!   dt = time step     dx = spatial grid size   c = wave speed
!   nmax = number of spatial units 
!   i runs from 0 to nmax, with the fixed ends at i=0 and i=nmax
sub propagate(y(,),dt,dx,c,nmax,bc,n1)
   r2 = (dt * c / dx)^2
   for i = 1 to nmax-1
      y(i,3) = r2 * (y(i+1,2) + y(i-1,2)) + 2*(1.0 - r2)*y(i,2) - y(i,1)
   next i
   if bc = 2 then
      y(0,3) = r2 * y(1,2) + (2.0 - r2)*y(0,2) - y(0,1)
      y(nmax,3) = r2 * y(nmax-1,2) + (2.0 - r2)*y(nmax,2) - y(nmax,1)
   end if
   for i = 0 to nmax
      y(i,1) = y(i,2)
      y(i,2) = y(i,3)
   next i
end sub

" display string profile
sub display(y(,),dx,nmax,color$,j,dt)
   set color "black"
   plot 0,-1.4;0,1.4
   plot 0,0;dx*nmax,0
   plot dx*nmax,-1.4;dx*nmax,1.4
   set cursor 2,10
   print "t = ";j*dt
   set color color$
   plot 0,y(0,2);
   for i = 1 to nmax-1    ! plot each interior grid point
      plot i * dx,y(i,2);
   next i 	
   plot nmax*dx,y(nmax,2)
end sub

sub axes(y(,),dx,nmax)
   set background color "white"
   set color "black"
   plot 0,-1.4;0,1.4
   plot 0,0;dx*nmax,0
   plot dx*nmax,-1.4;dx*nmax,1.4
end sub

! initialize variables   y(i,n) = string position at site i
! n = 3 = new position
! n = 2 = previous position
! n = 1 = position two time steps ago
! dt = time step   dx = spatial step   c = wave speed  
! nmax = number of grid steps
sub init(y(,),dt,dx,c,nmax,bc,n1,store$,sigma,x0,x1)
   input prompt "1 for fixed, 2 for free boundary -> ": bc
   input prompt "the string is 1 m long. dx (m) ? -> ": dx
   nmax = int(1/dx)
   dx = 1/nmax
   input prompt "time step dt (sec) ? -> ": dt
   input prompt "speed of propagation (m/s) -> ": c
   input prompt "initial (half) width of gaussian peak (m) -> ": sigma
   input prompt "initial position of the peak (from left) -> ": x0
   line input prompt "file to record data -> ": store$
   if store$ <> "" then input prompt "position to record y(t) at (from left) -> ": x1
   n1 = int(x1/dx)
   w = 1/(2*sigma^2)
   for i = 0 to nmax
      y(i,2) = exp(-w * (i * dx - x0 * nmax * dx)^2)  ! initial profile
      y(i,1) = y(i,2)
   next i
   if bc=1 then
      y(0,1)=0
      y(0,2)=0
      y(0,3)=0
      y(nmax,1)=0
      y(nmax,2)=0
      y(nmax,3)=0
   end if
end sub