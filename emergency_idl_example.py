#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file emergency_idl_examplefile.py
 @brief Python example implementations generated from emergency.idl
 @date $Date$


"""

import omniORB
from omniORB import CORBA, PortableServer
import _GlobalIDL, _GlobalIDL__POA


class Emergency_IDL_i (_GlobalIDL__POA.Emergency_IDL):
    """
    @class Emergency_IDL_i
    Example class implementing IDL interface Emergency_IDL
    """

    def __init__(self, rtc):
        """
        @brief standard constructor
        Initialise member variables here
        """
        self._rtc = rtc
        pass

    # void emergency()
    def emergency(self):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        print ' - Emergency.emergency() is called'
        self._rtc.setData(True)

if __name__ == "__main__":
    import sys
    
    # Initialise the ORB
    orb = CORBA.ORB_init(sys.argv)
    
    # As an example, we activate an object in the Root POA
    poa = orb.resolve_initial_references("RootPOA")

    # Create an instance of a servant class
    servant = Emergency_IDL_i()

    # Activate it in the Root POA
    poa.activate_object(servant)

    # Get the object reference to the object
    objref = servant._this()
    
    # Print a stringified IOR for it
    print orb.object_to_string(objref)

    # Activate the Root POA's manager
    poa._get_the_POAManager().activate()

    # Run the ORB, blocking this thread
    orb.run()

