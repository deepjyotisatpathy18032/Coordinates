#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from astropy import units as u
from astropy.coordinates import SkyCoord
c = SkyCoord('23:17:09.2366129', '+14:39:31.25621', unit=(u.hourangle, u.deg))
c.galactic

