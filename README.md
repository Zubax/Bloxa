Zubax Bloxa is the most compact ESC design that is possible using Mitochondrik module(at least it seems to be it). 

![Bloxa top](pics/bloxa_top.png)

![Bloxa bottom](pics/bloxa_bottom.png)

3D model for closer inspection is available in Autodesk online gallery https://gallery.autodesk.com/projects/146361/zubax-bloxa

Brief specs:

* Operating voltage range 4-8S Li-Po battery(15-34V)

* Continuous power 200W

* 1 UAVCAN interface

* RC PWM input available on test-pads(requires soldering)

  

  ![drawing](pics/bloxa_drawing.png)

  Bloxa power stage is uses  three [BUK9K6R2-40E](https://www.digikey.com/products/en?keywords=1727-7274-1-ND) MOSFET arrays. 

  | Parameter                              | Value            |
  | :------------------------------------- | ---------------- |
  | Drain to Source Voltage (Vdss)         | 40V              |
  | Current - Continuous Drain (Id) @ 25°C | 40A              |
  | Rds On (Max) @ Id, Vgs                 | 6mOhm @ 25A, 10V |
  | Gate Charge (Qg) (Max) @ Vgs           | 35.4nC @ 10V     |

  Current shunt value is 5 mOhm

  Bulk capacitor bank is formed with 3 180µF  aluminum electrolytic capacitors](https://www.digikey.com/products/en?keywords=565-4066-ND) from [ United Chemi-Con](https://www.digikey.com/en/supplier-centers/u/united-chemi-con).


## License

This project is licensed under the terms of [CC-BY-SA](https://creativecommons.org/licenses/by-sa/3.0/).
