\ Model Satisfaction
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  730 marketing_deivery + 800 recruiting + 700 training + 600 lenses
   + 400 color + 700 frame - 20 price
Subject To
 Customer_services: marketing_deivery + recruiting + training <= 2
 products: lenses + color + frame <= 2
 prices: price <= 200
 prices_1: price >= 90
 over_all: 730 marketing_deivery + 6000 recruiting + 5000 training
   + 4000 lenses + 3000 color + 5500 frame - 1000 price <= 10000
Bounds
Binaries
 marketing_deivery recruiting training lenses color frame
End
