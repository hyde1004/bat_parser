#### 목적 : BAT table의 채널 식별하기
#### 결과물 : Stream의 채널 정보 (TSID, ONID, Service ID)를 출력한다.
 - Bouquet ID
 - DVB Triplet (TSID, ONID, Service ID)
 - LCN (Logical Channel Number)

#### 출력

```
* filename : stream.ts
* BAT Info
    Version : 0x2
    Bouquet ID : 0x6070
      TSID : 0x0, ONID : 0x0, Service ID : 0x0, LCN : 100
    Bouquet ID : 0x6071
      TSID : 0x0, ONID : 0x0, Service ID : 0x0, LCN : 100
```

#### Test Stream : 11640_32700_20160901_partial.TRP
