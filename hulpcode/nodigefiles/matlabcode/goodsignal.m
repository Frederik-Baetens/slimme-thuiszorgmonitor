Signal = csvread('BVP.csv');

       % gesampeld @64 Hz

Signal(1:3) = [];

GoodSignal1 = Signal(6.195E5:6.196E5);

GoodSignal3 = Signal(6.195E5:6.277E5);

GoodSignal5 = Signal(6.195E5:6.2E5);

GoodSignal6 = Signal(6.195E5:6.277E5);

GoodSignal2 = Signal(6.2E4:7.76E4);

GoodSignal4 = Signal(2.2742E6:2.27555E6);

Signal = GoodSignal3;