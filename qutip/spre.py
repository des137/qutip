#This file is part of QuTIP.
#
#    QuTIP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#    QuTIP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with QuTIP.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2011, Paul D. Nation & Robert J. Johansson
#
###########################################################################
import scipy
import scipy.linalg as la
import scipy.sparse as sp
from scipy import prod, transpose, reshape
from Qobj import *
from istests import *
from operators import destroy, create
from basis import basis

def spre(A):
	if not isoper(A):
		raise TypeError('Input is not a quantum object')
	d=A.dims[1]
	S=Qobj()
	S.dims=[[A.dims[0][:],d[:]],[A.dims[1][:],d[:]]]
	S.shape=[prod(S.dims[0][0])*prod(S.dims[0][1]),prod(S.dims[1][0])*prod(S.dims[1][1])]
	S.data=sp.kron(sp.identity(prod(d)),A.data)
	return S
	

