# Python stubs generated by omniidl from idl/penkobu.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "_GlobalIDL"
#
__name__ = "_GlobalIDL"
_0__GlobalIDL = omniORB.openModule("_GlobalIDL", r"idl/penkobu.idl")
_0__GlobalIDL__POA = omniORB.openModule("_GlobalIDL__POA", r"idl/penkobu.idl")


# interface RunButton_IDL
_0__GlobalIDL._d_RunButton_IDL = (omniORB.tcInternal.tv_objref, "IDL:RunButton_IDL:1.0", "RunButton_IDL")
omniORB.typeMapping["IDL:RunButton_IDL:1.0"] = _0__GlobalIDL._d_RunButton_IDL
_0__GlobalIDL.RunButton_IDL = omniORB.newEmptyClass()
class RunButton_IDL :
    _NP_RepositoryId = _0__GlobalIDL._d_RunButton_IDL[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0__GlobalIDL.RunButton_IDL = RunButton_IDL
_0__GlobalIDL._tc_RunButton_IDL = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_RunButton_IDL)
omniORB.registerType(RunButton_IDL._NP_RepositoryId, _0__GlobalIDL._d_RunButton_IDL, _0__GlobalIDL._tc_RunButton_IDL)

# RunButton_IDL operations and attributes
RunButton_IDL._d_flush = ((), (), None)
RunButton_IDL._d_clear = ((), (), None)

# RunButton_IDL object reference
class _objref_RunButton_IDL (CORBA.Object):
    _NP_RepositoryId = RunButton_IDL._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def flush(self, *args):
        return _omnipy.invoke(self, "flush", _0__GlobalIDL.RunButton_IDL._d_flush, args)

    def clear(self, *args):
        return _omnipy.invoke(self, "clear", _0__GlobalIDL.RunButton_IDL._d_clear, args)

    __methods__ = ["flush", "clear"] + CORBA.Object.__methods__

omniORB.registerObjref(RunButton_IDL._NP_RepositoryId, _objref_RunButton_IDL)
_0__GlobalIDL._objref_RunButton_IDL = _objref_RunButton_IDL
del RunButton_IDL, _objref_RunButton_IDL

# RunButton_IDL skeleton
__name__ = "_GlobalIDL__POA"
class RunButton_IDL (PortableServer.Servant):
    _NP_RepositoryId = _0__GlobalIDL.RunButton_IDL._NP_RepositoryId


    _omni_op_d = {"flush": _0__GlobalIDL.RunButton_IDL._d_flush, "clear": _0__GlobalIDL.RunButton_IDL._d_clear}

RunButton_IDL._omni_skeleton = RunButton_IDL
_0__GlobalIDL__POA.RunButton_IDL = RunButton_IDL
omniORB.registerSkeleton(RunButton_IDL._NP_RepositoryId, RunButton_IDL)
del RunButton_IDL
__name__ = "_GlobalIDL"

#
# End of module "_GlobalIDL"
#
__name__ = "penkobu_idl"

_exported_modules = ( "_GlobalIDL", )

# The end.