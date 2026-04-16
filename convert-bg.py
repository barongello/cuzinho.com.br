#!/bin/env/python3
#-*- coding: utf-8 -*-

KEYS = [0x55, 0xAA]

with open('bg3.png', 'rb') as f:
  data = f.read()
  output = []
  ki = 0

  for i in data:
    output.append(i ^ KEYS[ki])
    ki ^= 1

  with open('bg.bin', 'wb') as o:
    o.write(bytes(output))

with open('bg.bin', 'rb') as f:
  data = f.read()
  output = []
  ki = 0

  for i in data:
    output.append(i ^ KEYS[ki])
    ki ^= 1

  with open('decrypted.png', 'wb') as o:
    o.write(bytes(output))
