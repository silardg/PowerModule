# PowerModule
## Main Components
### **TPS25970**
- Power supply: 10.8V - 13.2V (with UVLO and OVLO)
- Overcurrent protection: 7.7A

### **TPS62180**
- Used for 1.8V; 2.5V; 3.3V; 5V; output
- BGA package
- 6A maximum output

### **2074190081**




## Block Diagram
![Block Diagram](Docs/blockdiagram.drawio.png)

## PCB Views
![PCB Top](Docs/PowerModuleTop.png)
![PCB Bottom](Docs/PowerModuleBottom.png)

## Layers
Top Layer
![1](Docs/Layers/1.PNG)
2nd Layer
![1](Docs/Layers/2.PNG)
3rd Layer
![1](Docs/Layers/3.PNG)
Bottom Layer
![1](Docs/Layers/4.PNG)

## Power Analysis
![1](PowerModule/PDNAnalyzer_Output/PowerModule/Simulation/HTMLReport/ImagesCache/006.png)
![1](PowerModule/PDNAnalyzer_Output/PowerModule/Simulation/HTMLReport/ImagesCache/007.png)

The biggest concentration of current is with the eFuse. 
Only one of the regulators (the highest power one) was simulated, as others have the same layout and will have lower consumption than the 5V; 6A regulator. 