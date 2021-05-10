# Get System Information Metricbeat on Windows Servers

Tested on Windows 2019 and 2016
Metricbeat 7.12.0

## Get Disk Percentage

```
- module: windows
  metricsets: ["perfmom"]
  enabled: true
  period: 5m
  perfmom.queries:
    - object: '\Processor'
      namespace: processor
      instance: "*" (or 1,2,3,etc)
      counters:
        - name: '% Processor Time'
          label: time.processor.pct
        - name: '% User Time'
          label: time.user.pct
        - name: '% Interrupt Time'
          label: time.interrupt.pct
```

## Get Free Disk Percentage

```
- module: windows
  metricsets: ["perfmom"]
  enabled: true
  period: 5m
  perfmom.queries:
    - object: '\LogicalDisk'
      namespace: logicaldisk
      instance: "C:" (or "*" for all drives)
      counters:
        - name: '% Free Space'
          label: logicaldisk.free.space
```          
          
          
        
          

