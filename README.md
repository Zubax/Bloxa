# Zubax Bloxa

Zubax Bloxa is arguably the most compact practical ESC reference design based on [**Mitochondrik LV**](https://zubax.com/mitochondrik-lv). The key design requirements for Bloxa are:

* compactness;
* low mass;
* low COG;
* compatibility with the [UCANPHY standard](https://forum.opencyphal.org/t/cyphal-can-physical-layer-specification-v1-0/1471).

<img src="pics/bloxa.png" alt="Bloxa top"  width="100%" />

## Brief specs

* Operating voltage range: **4–8S** Li-ion (LiCoO<sub>2</sub>), 12–34 V
* Continuous power: **200 W**
* Single **Cyphal/CAN** interface
* Software-controllable **5V BEC** output connected to the CAN 5V line
* Aux port available on PCB pads (requires soldering); this port can be used for **RC PWM input** or for connecting the **motor temperature sensor**.
* Dimensions: 36.6x24.9 mm

The main advantage of Bloxa is its miniature size. To achieve it, a novel Mitochondrik mounting technique is used.

<p align="center">
<img src="pics/construction.png"  width = "50%"/>
</p>

Mitochondrik is mounted on the power stage PCB using an intermediary 2 mm thick PCB that serves as a connector.
Soldering is done using the edge connectors on the Mitochondrik, the intermediary  PCB, and the power stage PCB in the plane perpendicular to the PCB planes. 
Also, one of the RF shields on the Mitochondrik needs not be installed (Mitochondrik modules without the RF shield are available upon request, please contact Zubax Robotics).

<p align="center">
<img src="pics/drawing.png" alt="drawing"  width = "80%"/>
</p>

## Power stage details.

Bloxa power stage uses three BUK9K6R2-40E MOSFET arrays.

| Parameter                                               | Value               |
| :------------------------------------------------------ | ------------------- |
| Drain to Source Voltage (V<sub>ds</sub>)                | 40 V                |
| Current - Continuous Drain (I<sub>d</sub>) @ 25°C       | 40 A                |
| R<sub>ds on</sub> (Max) @ I<sub>d</sub>, V<sub>gs</sub> | 6 mOhm @ 25 A, 10 V |
| Gate Charge (Q<sub>g</sub>) (Max) @ V<sub>gs</sub>      | 35.4 nC @ 10 V      |

The bulk capacitor bank is formed with 3 [180 µF aluminum electrolytic capacitors](https://www.digikey.com/products/en?keywords=565-4066-ND) from [United Chemi-Con](https://www.digikey.com/en/supplier-centers/u/united-chemi-con).

## Release notes

Newest entries at the top.

### Bloxa v1.0

* Hardware over-current protection resistor has been adjusted in accordance with the latest design recommendations. See the [Mitochondrik LV](https://zubax.com/mitochondrik-lv) datasheet for details.
* Current shunts replaced with 3 mohms.

### Bloxa v0.2

* Current shunts replaced (5 mohms replaced with 10 mohms).
* Overcurrent protection added. Itrip is ~35 A.
* RCPWM through-hole connector replaced with smd solder pads.
* Power loss estimations table added to the schematic.
* TVS diode (D1) replaced with one that has lower breakdown voltage.

## License

This project is licensed under the terms of [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
