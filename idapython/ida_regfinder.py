"""
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_regfinder
else:
    import _ida_regfinder

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

SWIG_PYTHON_LEGACY_BOOL = _ida_regfinder.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

class reg_value_def_t(object):
    r"""
    Proxy of C++ reg_value_def_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    val = property(_ida_regfinder.reg_value_def_t_val_get, _ida_regfinder.reg_value_def_t_val_set, doc=r"""val""")
    r"""
    the value
    """
    def_ea = property(_ida_regfinder.reg_value_def_t_def_ea_get, _ida_regfinder.reg_value_def_t_def_ea_set, doc=r"""def_ea""")
    r"""
    the instruction address
    """
    def_itype = property(_ida_regfinder.reg_value_def_t_def_itype_get, _ida_regfinder.reg_value_def_t_def_itype_set, doc=r"""def_itype""")
    r"""
    the instruction code (processor specific)
    """
    flags = property(_ida_regfinder.reg_value_def_t_flags_get, _ida_regfinder.reg_value_def_t_flags_set, doc=r"""flags""")
    r"""
    additional info about the value
    """
    SHORT_INSN = property(_ida_regfinder.reg_value_def_t_SHORT_INSN_get, doc=r"""SHORT_INSN""")
    r"""
    like 'addi reg, imm'
    """
    PC_BASED = property(_ida_regfinder.reg_value_def_t_PC_BASED_get, doc=r"""PC_BASED""")
    r"""
    the value depends on DEF_EA only for numbers
    @see: is_num()
    """
    LIKE_GOT = property(_ida_regfinder.reg_value_def_t_LIKE_GOT_get, doc=r"""LIKE_GOT""")
    r"""
    the value is like GOT only for numbers
    @see: is_num()
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> reg_value_def_t
        __init__(self, _val, ea, _flags=0) -> reg_value_def_t

        @param _val: uval_t
        @param ea: ea_t
        @param _flags: uint16

        __init__(self, _val, insn, _flags=0) -> reg_value_def_t

        @param _val: uval_t
        @param insn: an ida_ua.insn_t, or an address (C++: const insn_t &)
        @param _flags: uint16
        """
        _ida_regfinder.reg_value_def_t_swiginit(self, _ida_regfinder.new_reg_value_def_t(*args))

    def is_short_insn(self, *args) -> "bool":
        r"""
        is_short_insn(self, insn) -> bool

        @param insn: an ida_ua.insn_t, or an address (C++: const insn_t &)

        is_short_insn(self) -> bool
        """
        return _ida_regfinder.reg_value_def_t_is_short_insn(self, *args)

    def is_pc_based(self, *args) -> "bool":
        r"""
        is_pc_based(self) -> bool
        """
        return _ida_regfinder.reg_value_def_t_is_pc_based(self, *args)

    def is_like_got(self, *args) -> "bool":
        r"""
        is_like_got(self) -> bool
        """
        return _ida_regfinder.reg_value_def_t_is_like_got(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: reg_value_def_t const &
        """
        return _ida_regfinder.reg_value_def_t___eq__(self, *args)

    def __lt__(self, *args) -> "bool":
        r"""
        __lt__(self, r) -> bool

        @param r: reg_value_def_t const &
        """
        return _ida_regfinder.reg_value_def_t___lt__(self, *args)
    NOVAL = _ida_regfinder.reg_value_def_t_NOVAL
    r"""
    without a value
    """
    
    UVAL = _ida_regfinder.reg_value_def_t_UVAL
    r"""
    as a number
    """
    
    SPVAL = _ida_regfinder.reg_value_def_t_SPVAL
    r"""
    as a SP delta
    """
    

    def dstr(self, *args) -> "qstring":
        r"""
        dstr(self, how, pm=None) -> qstring
        Return the string representation.

        @param how: (C++: dstr_val_t) enum reg_value_def_t::dstr_val_t
        @param pm: (C++: const procmod_t *) procmod_t const *
        """
        return _ida_regfinder.reg_value_def_t_dstr(self, *args)
    __swig_destroy__ = _ida_regfinder.delete_reg_value_def_t

# Register reg_value_def_t in _ida_regfinder:
_ida_regfinder.reg_value_def_t_swigregister(reg_value_def_t)
cvar = _ida_regfinder.cvar

class reg_value_info_t(object):
    r"""
    Proxy of C++ reg_value_info_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> reg_value_info_t
        """
        _ida_regfinder.reg_value_info_t_swiginit(self, _ida_regfinder.new_reg_value_info_t(*args))

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        Undefine the value.
        """
        return _ida_regfinder.reg_value_info_t_clear(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        Return 'true' if we know nothing about a value.
        """
        return _ida_regfinder.reg_value_info_t_empty(self, *args)

    @staticmethod
    def make_dead_end(*args) -> "reg_value_info_t":
        r"""
        make_dead_end(dead_end_ea) -> reg_value_info_t
        Return the undefined value because of a dead end.
        @see: is_dead_end()

        @param dead_end_ea: (C++: ea_t)
        """
        return _ida_regfinder.reg_value_info_t_make_dead_end(*args)

    @staticmethod
    def make_aborted(*args) -> "reg_value_info_t":
        r"""
        make_aborted(bblk_ea) -> reg_value_info_t
        Return the value after aborting.
        @see: aborted()

        @param bblk_ea: (C++: ea_t)
        """
        return _ida_regfinder.reg_value_info_t_make_aborted(*args)

    @staticmethod
    def make_badinsn(*args) -> "reg_value_info_t":
        r"""
        make_badinsn(insn_ea) -> reg_value_info_t
        Return the unknown value after a bad insn.
        @see: is_badinsn()

        @param insn_ea: (C++: ea_t)
        """
        return _ida_regfinder.reg_value_info_t_make_badinsn(*args)

    @staticmethod
    def make_unkinsn(*args) -> "reg_value_info_t":
        r"""
        make_unkinsn(insn) -> reg_value_info_t
        Return the unknown value after executing the insn.
        @see: is_unkinsn()

        @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
        """
        return _ida_regfinder.reg_value_info_t_make_unkinsn(*args)

    @staticmethod
    def make_unkfunc(*args) -> "reg_value_info_t":
        r"""
        make_unkfunc(func_ea) -> reg_value_info_t
        Return the unknown value from the function start.
        @see: is_unkfunc()

        @param func_ea: (C++: ea_t)
        """
        return _ida_regfinder.reg_value_info_t_make_unkfunc(*args)

    @staticmethod
    def make_unkloop(*args) -> "reg_value_info_t":
        r"""
        make_unkloop(bblk_ea) -> reg_value_info_t
        Return the unknown value if it changes in a loop.
        @see: is_unkloop()

        @param bblk_ea: (C++: ea_t)
        """
        return _ida_regfinder.reg_value_info_t_make_unkloop(*args)

    @staticmethod
    def make_unkmult(*args) -> "reg_value_info_t":
        r"""
        make_unkmult(bblk_ea) -> reg_value_info_t
        Return the unknown value if the register has incompatible values.
        @see: is_unkmult()

        @param bblk_ea: (C++: ea_t)
        """
        return _ida_regfinder.reg_value_info_t_make_unkmult(*args)

    @staticmethod
    def make_num(*args) -> "reg_value_info_t":
        r"""
        make_num(rval, insn, val_flags=0) -> reg_value_info_t
        Return the value that is the RVAL number.
        @see: is_num()

        @param rval: (C++: uval_t)
        @param insn: an ida_ua.insn_t, or an address (C++: const insn_t &)
        @param val_flags: (C++: uint16)

        make_num(rval, val_ea, val_flags=0) -> reg_value_info_t

        @param rval: uval_t
        @param val_ea: ea_t
        @param val_flags: uint16
        """
        return _ida_regfinder.reg_value_info_t_make_num(*args)

    @staticmethod
    def make_initial_sp(*args) -> "reg_value_info_t":
        r"""
        make_initial_sp(func_ea) -> reg_value_info_t
        Return the value that is the initial stack pointer.
        @see: is_spd()

        @param func_ea: (C++: ea_t)
        """
        return _ida_regfinder.reg_value_info_t_make_initial_sp(*args)

    def is_dead_end(self, *args) -> "bool":
        r"""
        is_dead_end(self) -> bool
        Return 'true' if the value is undefined because of a dead end.
        """
        return _ida_regfinder.reg_value_info_t_is_dead_end(self, *args)

    def aborted(self, *args) -> "bool":
        r"""
        aborted(self) -> bool
        Return 'true' if the tracking process was aborted.
        """
        return _ida_regfinder.reg_value_info_t_aborted(self, *args)

    def is_special(self, *args) -> "bool":
        r"""
        is_special(self) -> bool
        Return 'true' if the value requires special handling.
        """
        return _ida_regfinder.reg_value_info_t_is_special(self, *args)

    def is_badinsn(self, *args) -> "bool":
        r"""
        is_badinsn(self) -> bool
        Return 'true' if the value is unknown because of a bad insn.
        """
        return _ida_regfinder.reg_value_info_t_is_badinsn(self, *args)

    def is_unkinsn(self, *args) -> "bool":
        r"""
        is_unkinsn(self) -> bool
        Return 'true' if the value is unknown after executing the insn.
        """
        return _ida_regfinder.reg_value_info_t_is_unkinsn(self, *args)

    def is_unkfunc(self, *args) -> "bool":
        r"""
        is_unkfunc(self) -> bool
        Return 'true' if the value is unknown from the function start.
        """
        return _ida_regfinder.reg_value_info_t_is_unkfunc(self, *args)

    def is_unkloop(self, *args) -> "bool":
        r"""
        is_unkloop(self) -> bool
        Return 'true' if the value is unknown because it changes in a loop.
        """
        return _ida_regfinder.reg_value_info_t_is_unkloop(self, *args)

    def is_unkmult(self, *args) -> "bool":
        r"""
        is_unkmult(self) -> bool
        Return 'true' if the value is unknown because the register has incompatible
        values (a number and SP delta).
        """
        return _ida_regfinder.reg_value_info_t_is_unkmult(self, *args)

    def is_unknown(self, *args) -> "bool":
        r"""
        is_unknown(self) -> bool
        Return 'true' if the value is unknown.
        """
        return _ida_regfinder.reg_value_info_t_is_unknown(self, *args)

    def is_num(self, *args) -> "bool":
        r"""
        is_num(self) -> bool
        Return 'true' if the value is a constant.
        """
        return _ida_regfinder.reg_value_info_t_is_num(self, *args)

    def is_spd(self, *args) -> "bool":
        r"""
        is_spd(self) -> bool
        Return 'true' if the value depends on the stack pointer.
        """
        return _ida_regfinder.reg_value_info_t_is_spd(self, *args)

    def is_known(self, *args) -> "bool":
        r"""
        is_known(self) -> bool
        Return 'true' if the value is known (i.e. it is a number or SP delta).
        """
        return _ida_regfinder.reg_value_info_t_is_known(self, *args)

    def get_num(self, *args) -> "bool":
        r"""
        get_num(self) -> bool
        Return the number if the value is a constant.
        @see: is_num()
        """
        return _ida_regfinder.reg_value_info_t_get_num(self, *args)

    def get_spd(self, *args) -> "bool":
        r"""
        get_spd(self) -> bool
        Return the SP delta if the value depends on the stack pointer.
        @see: is_spd()
        """
        return _ida_regfinder.reg_value_info_t_get_spd(self, *args)

    def get_def_ea(self, *args) -> "ea_t":
        r"""
        get_def_ea(self) -> ea_t
        Return the defining address.
        """
        return _ida_regfinder.reg_value_info_t_get_def_ea(self, *args)

    def get_def_itype(self, *args) -> "uint16":
        r"""
        get_def_itype(self) -> uint16
        Return the defining instruction code (processor specific).
        """
        return _ida_regfinder.reg_value_info_t_get_def_itype(self, *args)

    def is_value_unique(self, *args) -> "bool":
        r"""
        is_value_unique(self) -> bool
        Check that the value is unique.
        """
        return _ida_regfinder.reg_value_info_t_is_value_unique(self, *args)

    def have_all_vals_flag(self, *args) -> "bool":
        r"""
        have_all_vals_flag(self, val_flags) -> bool
        Check the given flag for each value.

        @param val_flags: (C++: uint16)
        """
        return _ida_regfinder.reg_value_info_t_have_all_vals_flag(self, *args)

    def is_all_vals_pc_based(self, *args) -> "bool":
        r"""
        is_all_vals_pc_based(self) -> bool
        """
        return _ida_regfinder.reg_value_info_t_is_all_vals_pc_based(self, *args)

    def is_all_vals_like_got(self, *args) -> "bool":
        r"""
        is_all_vals_like_got(self) -> bool
        """
        return _ida_regfinder.reg_value_info_t_is_all_vals_like_got(self, *args)

    def set_dead_end(self, *args) -> "void":
        r"""
        set_dead_end(self, dead_end_ea)
        Set the value to be undefined because of a dead end.
        @see: is_dead_end()

        @param dead_end_ea: (C++: ea_t)
        """
        return _ida_regfinder.reg_value_info_t_set_dead_end(self, *args)

    def set_badinsn(self, *args) -> "void":
        r"""
        set_badinsn(self, insn_ea)
        Set the value to be unknown after a bad insn.
        @see: is_badinsn()

        @param insn_ea: (C++: ea_t)
        """
        return _ida_regfinder.reg_value_info_t_set_badinsn(self, *args)

    def set_unkinsn(self, *args) -> "void":
        r"""
        set_unkinsn(self, insn)
        Set the value to be unknown after executing the insn.
        @see: is_unkinsn()

        @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
        """
        return _ida_regfinder.reg_value_info_t_set_unkinsn(self, *args)

    def set_unkfunc(self, *args) -> "void":
        r"""
        set_unkfunc(self, func_ea)
        Set the value to be unknown from the function start.
        @see: is_unkfunc()

        @param func_ea: (C++: ea_t)
        """
        return _ida_regfinder.reg_value_info_t_set_unkfunc(self, *args)

    def set_unkloop(self, *args) -> "void":
        r"""
        set_unkloop(self, bblk_ea)
        Set the value to be unknown because it changes in a loop.
        @see: is_unkloop()

        @param bblk_ea: (C++: ea_t)
        """
        return _ida_regfinder.reg_value_info_t_set_unkloop(self, *args)

    def set_unkmult(self, *args) -> "void":
        r"""
        set_unkmult(self, bblk_ea)
        Set the value to be unknown because the register has incompatible values.
        @see: is_unkmult()

        @param bblk_ea: (C++: ea_t)
        """
        return _ida_regfinder.reg_value_info_t_set_unkmult(self, *args)

    def set_aborted(self, *args) -> "void":
        r"""
        set_aborted(self, bblk_ea)
        Set the value after aborting.
        @see: aborted()

        @param bblk_ea: (C++: ea_t)
        """
        return _ida_regfinder.reg_value_info_t_set_aborted(self, *args)

    def set_num(self, *args) -> "void":
        r"""
        set_num(self, rval, insn, val_flags=0)
        Set the value to be a number before an address.
        @see: is_num()

        @param rval: (C++: uval_t)
        @param insn: an ida_ua.insn_t, or an address (C++: const insn_t &)
        @param val_flags: (C++: uint16)

        set_num(self, rvals, insn)

        @param rvals: uvalvec_t *
        @param insn: an ida_ua.insn_t, or an address (C++: const insn_t &)

        set_num(self, rval, val_ea, val_flags=0)

        @param rval: uval_t
        @param val_ea: ea_t
        @param val_flags: uint16
        """
        return _ida_regfinder.reg_value_info_t_set_num(self, *args)
    EQUAL = _ida_regfinder.reg_value_info_t_EQUAL
    r"""
    L==R.
    """
    
    CONTAINS = _ida_regfinder.reg_value_info_t_CONTAINS
    r"""
    L contains R (i.e. R\L is empty)
    """
    
    CONTAINED = _ida_regfinder.reg_value_info_t_CONTAINED
    r"""
    L is contained in R (i.e. L\R is empty)
    """
    
    NOT_COMPARABLE = _ida_regfinder.reg_value_info_t_NOT_COMPARABLE
    r"""
    L\R is not empty and R\L is not empty.
    """
    

    def vals_union(self, *args) -> "reg_value_info_t::set_compare_res_t":
        r"""
        vals_union(self, r) -> reg_value_info_t::set_compare_res_t
        Add values from R into THIS ignoring duplicates.
        @note: This method is the only way to get multiple values.
        @retval EQUAL: THIS is not changed
        @retval CONTAINS: THIS is not changed
        @retval CONTAINED: THIS is a copy of R
        @retval NOT_COMPARABLE: values from R are added to THIS

        @param r: (C++: const reg_value_info_t &) reg_value_info_t const &
        """
        return _ida_regfinder.reg_value_info_t_vals_union(self, *args)

    def extend(self, *args) -> "void":
        r"""
        extend(self, pm, width, is_signed)
        Sign-, or zero-extend the number or SP delta value to full size. The initial
        value is considered to be of size WIDTH.
        @note: This method do nothing for unknown values.

        @param pm: (C++: const procmod_t &) procmod_t const &
        @param width: (C++: int)
        @param is_signed: (C++: bool)
        """
        return _ida_regfinder.reg_value_info_t_extend(self, *args)

    def trunc_uval(self, *args) -> "void":
        r"""
        trunc_uval(self, pm)
        Truncate the number to the application bitness.
        @note: This method do nothing for non-number values.

        @param pm: (C++: const procmod_t &) procmod_t const &
        """
        return _ida_regfinder.reg_value_info_t_trunc_uval(self, *args)
    ADD = _ida_regfinder.reg_value_info_t_ADD
    
    SUB = _ida_regfinder.reg_value_info_t_SUB
    
    OR = _ida_regfinder.reg_value_info_t_OR
    
    AND = _ida_regfinder.reg_value_info_t_AND
    
    XOR = _ida_regfinder.reg_value_info_t_XOR
    
    AND_NOT = _ida_regfinder.reg_value_info_t_AND_NOT
    
    SLL = _ida_regfinder.reg_value_info_t_SLL
    
    SLR = _ida_regfinder.reg_value_info_t_SLR
    
    NEG = _ida_regfinder.reg_value_info_t_NEG
    
    NOT = _ida_regfinder.reg_value_info_t_NOT
    

    def add(self, *args) -> "void":
        r"""
        add(self, r, insn)
        Add R to the value, save INSN as a defining instruction.
        @note: Either THIS or R must have a single value.

        @param r: (C++: const reg_value_info_t &) reg_value_info_t const &
        @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
        """
        return _ida_regfinder.reg_value_info_t_add(self, *args)

    def sub(self, *args) -> "void":
        r"""
        sub(self, r, insn)
        Subtract R from the value, save INSN as a defining instruction.
        @note: Either THIS or R must have a single value.

        @param r: (C++: const reg_value_info_t &) reg_value_info_t const &
        @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
        """
        return _ida_regfinder.reg_value_info_t_sub(self, *args)

    def bor(self, *args) -> "void":
        r"""
        bor(self, r, insn)
        Make bitwise OR of R to the value, save INSN as a defining instruction.
        @note: Either THIS or R must have a single value.

        @param r: (C++: const reg_value_info_t &) reg_value_info_t const &
        @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
        """
        return _ida_regfinder.reg_value_info_t_bor(self, *args)

    def band(self, *args) -> "void":
        r"""
        band(self, r, insn)
        Make bitwise AND of R to the value, save INSN as a defining instruction.
        @note: Either THIS or R must have a single value.

        @param r: (C++: const reg_value_info_t &) reg_value_info_t const &
        @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
        """
        return _ida_regfinder.reg_value_info_t_band(self, *args)

    def bxor(self, *args) -> "void":
        r"""
        bxor(self, r, insn)
        Make bitwise eXclusive OR of R to the value, save INSN as a defining
        instruction.
        @note: Either THIS or R must have a single value.

        @param r: (C++: const reg_value_info_t &) reg_value_info_t const &
        @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
        """
        return _ida_regfinder.reg_value_info_t_bxor(self, *args)

    def bandnot(self, *args) -> "void":
        r"""
        bandnot(self, r, insn)
        Make bitwise AND of the inverse of R to the value, save INSN as a defining
        instruction.
        @note: Either THIS or R must have a single value.

        @param r: (C++: const reg_value_info_t &) reg_value_info_t const &
        @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
        """
        return _ida_regfinder.reg_value_info_t_bandnot(self, *args)

    def sll(self, *args) -> "void":
        r"""
        sll(self, r, insn)
        Shift the value left by R, save INSN as a defining instruction.
        @note: Either THIS or R must have a single value.

        @param r: (C++: const reg_value_info_t &) reg_value_info_t const &
        @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
        """
        return _ida_regfinder.reg_value_info_t_sll(self, *args)

    def slr(self, *args) -> "void":
        r"""
        slr(self, r, insn)
        Shift the value right by R, save INSN as a defining instruction.
        @note: Either THIS or R must have a single value.

        @param r: (C++: const reg_value_info_t &) reg_value_info_t const &
        @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
        """
        return _ida_regfinder.reg_value_info_t_slr(self, *args)

    def neg(self, *args) -> "void":
        r"""
        neg(self, insn)
        Negate the value, save INSN as a defining instruction.

        @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
        """
        return _ida_regfinder.reg_value_info_t_neg(self, *args)

    def bnot(self, *args) -> "void":
        r"""
        bnot(self, insn)
        Make bitwise inverse of the value, save INSN as a defining instruction.

        @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
        """
        return _ida_regfinder.reg_value_info_t_bnot(self, *args)

    def add_num(self, *args) -> "void":
        r"""
        add_num(self, r, insn)
        Add R to the value, do not change the defining instructions.
        @note: This method do nothing for unknown values.

        @param r: (C++: uval_t)
        @param insn: an ida_ua.insn_t, or an address (C++: const insn_t &)

        add_num(self, r)

        @param r: uval_t
        """
        return _ida_regfinder.reg_value_info_t_add_num(self, *args)

    def shift_left(self, *args) -> "void":
        r"""
        shift_left(self, r)
        Shift the value left by R, do not change the defining instructions.
        @note: This method do nothing for unknown values.

        @param r: (C++: uval_t)
        """
        return _ida_regfinder.reg_value_info_t_shift_left(self, *args)

    def shift_right(self, *args) -> "void":
        r"""
        shift_right(self, r)
        Shift the value right by R, do not change the defining instructions.
        @note: This method do nothing for unknown values.

        @param r: (C++: uval_t)
        """
        return _ida_regfinder.reg_value_info_t_shift_right(self, *args)

    def __str__(self, *args) -> "qstring":
        r"""
        __str__(self) -> qstring
        """
        return _ida_regfinder.reg_value_info_t___str__(self, *args)

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_regfinder.reg_value_info_t___len__(self, *args)

    def __getitem__(self, *args) -> "reg_value_def_t const &":
        r"""
        __getitem__(self, i) -> reg_value_def_t

        @param i: size_t
        """
        return _ida_regfinder.reg_value_info_t___getitem__(self, *args)
    __swig_destroy__ = _ida_regfinder.delete_reg_value_info_t

# Register reg_value_info_t in _ida_regfinder:
_ida_regfinder.reg_value_info_t_swigregister(reg_value_info_t)

def reg_value_info_t_make_dead_end(*args) -> "reg_value_info_t":
    r"""
    reg_value_info_t_make_dead_end(dead_end_ea) -> reg_value_info_t

    @param dead_end_ea: ea_t
    """
    return _ida_regfinder.reg_value_info_t_make_dead_end(*args)

def reg_value_info_t_make_aborted(*args) -> "reg_value_info_t":
    r"""
    reg_value_info_t_make_aborted(bblk_ea) -> reg_value_info_t

    @param bblk_ea: ea_t
    """
    return _ida_regfinder.reg_value_info_t_make_aborted(*args)

def reg_value_info_t_make_badinsn(*args) -> "reg_value_info_t":
    r"""
    reg_value_info_t_make_badinsn(insn_ea) -> reg_value_info_t

    @param insn_ea: ea_t
    """
    return _ida_regfinder.reg_value_info_t_make_badinsn(*args)

def reg_value_info_t_make_unkinsn(*args) -> "reg_value_info_t":
    r"""
    reg_value_info_t_make_unkinsn(insn) -> reg_value_info_t

    @param insn: an ida_ua.insn_t, or an address (C++: const insn_t &)
    """
    return _ida_regfinder.reg_value_info_t_make_unkinsn(*args)

def reg_value_info_t_make_unkfunc(*args) -> "reg_value_info_t":
    r"""
    reg_value_info_t_make_unkfunc(func_ea) -> reg_value_info_t

    @param func_ea: ea_t
    """
    return _ida_regfinder.reg_value_info_t_make_unkfunc(*args)

def reg_value_info_t_make_unkloop(*args) -> "reg_value_info_t":
    r"""
    reg_value_info_t_make_unkloop(bblk_ea) -> reg_value_info_t

    @param bblk_ea: ea_t
    """
    return _ida_regfinder.reg_value_info_t_make_unkloop(*args)

def reg_value_info_t_make_unkmult(*args) -> "reg_value_info_t":
    r"""
    reg_value_info_t_make_unkmult(bblk_ea) -> reg_value_info_t

    @param bblk_ea: ea_t
    """
    return _ida_regfinder.reg_value_info_t_make_unkmult(*args)

def reg_value_info_t_make_num(*args) -> "reg_value_info_t":
    r"""
    reg_value_info_t_make_num(rval, insn, val_flags=0) -> reg_value_info_t

    @param rval: uval_t
    @param insn: an ida_ua.insn_t, or an address (C++: const insn_t &)
    @param val_flags: uint16

    reg_value_info_t_make_num(rval, val_ea, val_flags=0) -> reg_value_info_t

    @param rval: uval_t
    @param val_ea: ea_t
    @param val_flags: uint16
    """
    return _ida_regfinder.reg_value_info_t_make_num(*args)

def reg_value_info_t_make_initial_sp(*args) -> "reg_value_info_t":
    r"""
    reg_value_info_t_make_initial_sp(func_ea) -> reg_value_info_t

    @param func_ea: ea_t
    """
    return _ida_regfinder.reg_value_info_t_make_initial_sp(*args)


def find_reg_value(*args) -> "uint64 *":
    r"""
    find_reg_value(ea, reg) -> int
    Find register value using the register tracker.
    @note: The returned value is valid *before* executing the instruction.

    @param ea: (C++: ea_t) the address to find a value at
    @param reg: (C++: int) the register to find
    @retval 0: no value (the value is varying or the find depth is not enough to
               find a value)
    @retval 1: the found value is in VAL
    @retval -1: the processor module does not support a register tracker
    """
    return _ida_regfinder.find_reg_value(*args)

def find_sp_value(*args) -> "int64 *":
    r"""
    find_sp_value(ea, reg=-1) -> int
    Find a value of the SP based register using the register tracker.
    @note: The returned value is valid *before* executing the instruction.

    @param ea: (C++: ea_t) the address to find a value at
    @param reg: (C++: int) the register to find. by default the SP register is used.
    @retval 0: no value (the value is varying or the find depth is not enough to
               find a value)
    @retval 1: the found value is in VAL
    @retval -1: the processor module does not support a register tracker
    """
    return _ida_regfinder.find_sp_value(*args)

def find_reg_value_info(*args) -> "bool":
    r"""
    find_reg_value_info(rvi, ea, reg, max_depth=0) -> bool
    Find register value using the register tracker.
    @note: The returned value is valid *before* executing the instruction.
    @note: The _undefined_ value means that there is no execution flow to EA, e.g.
           we try to find a value after the call of NORET function.
    @note: The _unknown_ value means that the value is:
    * a result of unsupported instruction, e.g. the result of a call,
    * a function argument,
    * is varying, e.g. it is a loop counter.

    @param rvi: (C++: reg_value_info_t *) the found value with additional attributes
    @param ea: (C++: ea_t) the address to find a value at
    @param reg: (C++: int) the register to find
    @param max_depth: (C++: int) the number of basic blocks to look before aborting the search
                      and returning the unknown value. 0 means the value of
                      REGTRACK_MAX_DEPTH from ida.cfg for ordinal registers or
                      REGTRACK_FUNC_MAX_DEPTH for the function-wide registers, -1
                      means the value of REGTRACK_FUNC_MAX_DEPTH from ida.cfg.
    @retval 'false': the processor module does not support a register tracker
    @retval 'true': the found value is in RVI
    """
    return _ida_regfinder.find_reg_value_info(*args)

def find_nearest_rvi(*args) -> "int":
    r"""
    find_nearest_rvi(rvi, ea, reg) -> int
    Find the value of any of the two registers using the register tracker. First,
    this function tries to find the registers in the basic block of EA, and if it
    could not do this, then it tries to find in the entire function.

    @param rvi: (C++: reg_value_info_t *) the found value with additional attributes
    @param ea: (C++: ea_t) the address to find a value at
    @param reg: (C++: const int) the registers to find
    @return: the index of the found register or -1
    """
    return _ida_regfinder.find_nearest_rvi(*args)

def invalidate_regfinder_cache(*args) -> "void":
    r"""
    invalidate_regfinder_cache(ea=BADADDR)
    Remove from the register tracker cache all values at EA and all dependent
    values. As if the control flow to this instruction has changed. if EA == BADADDR
    then clear the entire cache.

    @param ea: (C++: ea_t)
    """
    return _ida_regfinder.invalidate_regfinder_cache(*args)



