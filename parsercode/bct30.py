# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_bct30', [dirname(__file__)])
        except ImportError:
            import _bct30
            return _bct30
        if fp is not None:
            try:
                _mod = imp.load_module('_bct30', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _bct30 = swig_import_helper()
    del swig_import_helper
else:
    import _bct30
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class bct30(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, bct30, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, bct30, name)
    __repr__ = _swig_repr
    def getEncoderCnt(self, *args): return _bct30.bct30_getEncoderCnt(self, *args)
    def getPosition(self, *args): return _bct30.bct30_getPosition(self, *args)
    def getVelocity(self, *args): return _bct30.bct30_getVelocity(self, *args)
    def getDigitalIO(self, *args): return _bct30.bct30_getDigitalIO(self, *args)
    def TranslateError(self, *args): return _bct30.bct30_TranslateError(self, *args)
    def GetError(self): return _bct30.bct30_GetError(self)
    def setZenith(self): return _bct30.bct30_setZenith(self)
    def setPosition(self, *args): return _bct30.bct30_setPosition(self, *args)
    def stopSlew(self, *args): return _bct30.bct30_stopSlew(self, *args)
    def estop(self, *args): return _bct30.bct30_estop(self, *args)
    def enableAmp(self, *args): return _bct30.bct30_enableAmp(self, *args)
    def IsAtTarget(self, *args): return _bct30.bct30_IsAtTarget(self, *args)
    def IsStopped(self, *args): return _bct30.bct30_IsStopped(self, *args)
    def MoveRelative(self, *args): return _bct30.bct30_MoveRelative(self, *args)
    def Jog(self, *args): return _bct30.bct30_Jog(self, *args)
    def moveTo(self, *args): return _bct30.bct30_moveTo(self, *args)
    def MoveAbsolute(self, *args): return _bct30.bct30_MoveAbsolute(self, *args)
    def track(self, *args): return _bct30.bct30_track(self, *args)
    def moveRelativeDegrees(self, *args): return _bct30.bct30_moveRelativeDegrees(self, *args)
    def checkHandPaddle(self): return _bct30.bct30_checkHandPaddle(self)
    def checkHandPaddle2(self): return _bct30.bct30_checkHandPaddle2(self)
    def GetFollowingError(self, *args): return _bct30.bct30_GetFollowingError(self, *args)
    def Reset(self, *args): return _bct30.bct30_Reset(self, *args)
    def getStatus(self, *args): return _bct30.bct30_getStatus(self, *args)
    def getMode(self, *args): return _bct30.bct30_getMode(self, *args)
    def __init__(self): 
        this = _bct30.new_bct30()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bct30.delete_bct30
    __del__ = lambda self : None;
bct30_swigregister = _bct30.bct30_swigregister
bct30_swigregister(bct30)

# This file is compatible with both classic and new-style classes.


