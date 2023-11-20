# convexlib


```
pip install git+https://github.com/convexvalue/convexlib.git
```

```py
from convexlib.api import ConvexApi

# use "pro" or "live"
convex_instance = ConvexApi("your_email", "your_password","pro")

# requesting underlyings
und_data = convex_instance.get_und(symbols=["SPX","AAPL"],params=["price","value"])

# response:
# {'data': [['SPX', 4500.65, 5243084535.0], ['AAPL', 186.8301, 90424357.0]] }





# requesting option chain
chain = convex_instance.get_chain("AAPL",params=["volm_bs","volatility"],exps=[1,2,3],rng=0.10)

# requesting option chain as rows
rows = convex_instance.get_chain_as_rows("AAPL",params=["volm_bs","volatility"],exps=[1,2,3],rng=0.10)
# response
# [symbol,expiration,strike,kind,...params]
```


## `get_und` Parameters

```
multiplier          
product             
event_time                  
day_id                      
day_open_price              
day_high_price              
day_low_price               
day_close_price             
day_close_price_type        
prev_day_id                 
prev_day_close_price        
prev_day_close_price_type   
prev_day_volume             
oi                          
short_sale_restriction      
trading_status              
halt_start_time             
halt_end_time               
high_limit_price            
low_limit_price             
high_52_week_price          
low_52_week_price           
bid_time                    
bid_exchange_code           
bid_price                   
bid_size                    
ask_time                    
ask_exchange_code           
ask_price                   
ask_size                    
t_time                      
sequence                    
exchange_code               
price                       
change                      
size                        
t_day_id                    
day_volume                  
day_turnover                
tick_direction              
extended_trading_hours      
u_index                     
u_time                      
u_sequence                  
volatility                  
front_volatility            
back_volatility             
call_volume                 
put_volume                  
put_call_ratio              
option_volume               
expiration                  
value                           
volm                            
deltas                          
gammas                          
vegas                           
thetas                          
rhos                            
value_buy                       
volm_buy                        
deltas_buy                      
gammas_buy                      
vegas_buy                       
thetas_buy                      
rhos_buy                        
value_call_buy                  
volm_call_buy                   
deltas_call_buy                 
gammas_call_buy                 
vegas_call_buy                  
thetas_call_buy                 
rhos_call_buy                   
value_put_buy                   
volm_put_buy                    
deltas_put_buy                  
gammas_put_buy                  
vegas_put_buy                   
thetas_put_buy                  
rhos_put_buy                    
value_sell                      
volm_sell                       
deltas_sell                     
gammas_sell                     
vegas_sell                      
thetas_sell                     
rhos_sell                       
value_call_sell                 
volm_call_sell                  
deltas_call_sell                
gammas_call_sell                
vegas_call_sell                 
thetas_call_sell                
rhos_call_sell                  
value_put_sell                  
volm_put_sell                   
deltas_put_sell                 
gammas_put_sell                 
vegas_put_sell                  
thetas_put_sell                 
rhos_put_sell                   
value_und                       
volm_und                        
deltas_und                      
gammas_und                      
vegas_und                       
thetas_und                      
rhos_und                        
value_call_und                  
volm_call_und                   
deltas_call_und                 
gammas_call_und                 
vegas_call_und                  
thetas_call_und                 
rhos_call_und                   
value_put_und                   
volm_put_und                    
deltas_put_und                  
gammas_put_und                  
vegas_put_und                   
thetas_put_und                  
rhos_put_und                    
value_bs                        
volm_bs                         
flowratio                       
vflowratio                      
value_call_ratio                
value_put_ratio                 
volm_call_ratio                 
volm_put_ratio                  
value_call_bs                   
value_put_bs                    
volm_call_bs                    
volm_put_bs                     
flownet                         
vflownet                        
prop1                           
prop2                           
prop3                           
prop4                           
dxoi                            
dxoi2                           
gxoi                            
vxoi                            
txoi                            
vannaxoi                        
charmxoi                        
gxvolm                          
vxvolm                          
txvolm                          
vannaxvolm                      
charmxvolm                      
dxvolm                          
dxvolm2                         
call_dxoi                       
call_gxoi                       
call_vxoi                       
call_txoi                       
put_dxoi                        
put_gxoi                        
put_vxoi                        
put_txoi                        
```

---

## `get_chain` Parameters


```
opt_kind            
expiration          
multiplier          
product             
expiration_ts       
underlying              
strike                  
g_time                  
theo                    
volatility              
delta                   
gamma                   
theta                   
rho                     
vega                    
event_time                  
day_id                      
day_open_price              
day_high_price              
day_low_price               
day_close_price             
day_close_price_type        
prev_day_id                 
prev_day_close_price        
prev_day_close_price_type   
prev_day_volume             
oi                          
oi_ch                       
bid_time                    
bid_exchange_code           
bid_price                   
bid_size                    
ask_time                    
ask_exchange_code           
ask_price                   
ask_size                    
spread                      
t_time                      
sequence                    
exchange_code               
price                       
change                      
size                        
day_volume                  
day_turnover                
tick_direction              
extended_trading_hours      
tas_last_time                   
value                           
volm                            
deltas                          
gammas                          
vegas                           
thetas                          
rhos                            
value_buy                       
volm_buy                        
deltas_buy                      
gammas_buy                      
vegas_buy                       
thetas_buy                      
rhos_buy                        
value_sell                      
volm_sell                       
deltas_sell                     
gammas_sell                     
vegas_sell                      
thetas_sell                     
rhos_sell                       
value_und                       
volm_und                        
deltas_und                      
gammas_und                      
vegas_und                       
thetas_und                      
rhos_und                        
value_bs                        
volm_bs                         
vanna                           
vomma                           
charm                           
dxoi                            
gxoi                            
vxoi                            
txoi                            
vannaxoi                        
vommaxoi                        
charmxoi                        
gxvolm                          
vxvolm                          
txvolm                          
dxvolm                          
vannaxvolm                      
vommaxvolm                      
charmxvolm                      
volm_5m     
value_5m    
volmbs_5m   
valuebs_5m  
volm_15m    
value_15m   
volmbs_15m  
valuebs_15m
volm_30m    
value_30m   
volmbs_30m  
valuebs_30m
volm_60m    
value_60m   
volmbs_60m  
valuebs_60m
```
