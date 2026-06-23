raw_yield = [120, -45, 300, 0, 450, -12, 180, 600, 85]
filtered_yields = [ round(x, 1) for x in raw_yield if x > 0 ]
scaled_yields = [ round (f_yield*1.15, 1) for f_yield in filtered_yields]
analysed_yields = [ round (y*1.15, 1) for y in raw_yield if y > 0 ]

dashboard = f"""
==========================================
             YIELD DASHBOARD
==========================================
Raw Data Count       : {len(raw_yield)}
Raw Yield Values     : {raw_yield}
------------------------------------------
Sanitized Data Count : {len(filtered_yields)}
Sanitized Yields     : {filtered_yields}
Optimized Yields (1.15x) : {scaled_yields}
------------------------------------------
Master Compact Yields: {analysed_yields}
==========================================
"""
print(dashboard)
