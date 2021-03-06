# -*- coding: utf-8 -*-
'''
.. moduleauthor:: Sascha Eichstaedt (sascha.eichstaedt@ptb.de)
'''
if __name__=="identification.fit_filter": # module is imported from within package
    from misc.filterstuff import grpdelay, mapinside
else:
    from ..misc.filterstuff import grpdelay, mapinside


def LSIIR(Hvals,Nb,Na,f,Fs,tau=0,justFit=False):
    """Least-squares IIR filter fit to a given frequency response
    
    This method uses Gauss-Newton non-linear optimization and pole mapping for filter stabilization
    
    Parameters:
        Hvals:   ndarray
                 frequency response values
        Nb:      int
                 numerator polynomial order
        Na:      int 
                 denominator polynomial order
        f:       ndarray
                 frequencies
        Fs:      float
                 sampling frequency
        tau:     int
                 initial time delay
        justFit: boolean
                 whether to do stabilization
    
    Returns:
        b,a:    ndarray
                IIR filter coefficients 
        tau:    int
                filter time delay in samples
    
    References:
    * Eichstädt et al. 2010 [Eichst2010]_
    * Vuerinckx et al. 1996 [Vuer1996]_
    
    """
    from numpy import exp,pi,arange,newaxis,dot,diag,hstack,real,conj,imag
    from numpy import count_nonzero,roots,ceil,median,sqrt
    from numpy.linalg import lstsq
    from scipy.signal import freqz

    print "\nLeast-squares fit of an order %d digital IIR filter" % max(Nb,Na)
    print "to a frequency response given by %d values.\n" % len(Hvals)
  
    w = 2*pi*f/Fs
    Ns= arange(0,max(Nb,Na)+1)[:,newaxis]
    E = exp(-1j*dot(w[:,newaxis],Ns.T))
    
    def fitIIR(Hvals,tau,E,Na,Nb):
        Ea= E[:,1:Na+1]
        Eb= E[:,:Nb+1]
        Htau = exp(-1j*w*tau)*Hvals
        HEa = dot(diag(Htau),Ea)
        D   = hstack((HEa,-Eb))
        Tmp1= real(dot(conj(D.T),D))
        Tmp2= real(dot(conj(D.T),-Htau))
        ab = lstsq(Tmp1,Tmp2)[0]
        a = hstack((1.0,ab[:Na]))
        b = ab[Na:]
        return b,a
        
    b,a = fitIIR(Hvals,tau,E,Na,Nb)
    
    if justFit:        
        print "Calculation done. No stabilization requested."
        if count_nonzero(abs(roots(a))>1)>0:
            print "Obtained filter is NOT stable."
        sos = sum( abs( (freqz(b,a,2*pi*f/Fs)[1]-Hvals)**2 ) )
        print "Final sum of squares = %e" % sos
        tau = 0
        return b,a,tau
    
    if count_nonzero(abs(roots(a))>1)>0:
        stable = False
    else:
        stable = True
    
    maxiter = 50
    
    astab = mapinside(a)
    run = 1
    
    while stable!=True and run < maxiter:
        g1 = grpdelay(b,a,Fs)[0]
        g2 = grpdelay(b,astab,Fs)[0]
        tau = ceil(tau + median(g2-g1))
        
        b,a = fitIIR(Hvals,tau,E,Na,Nb)
        if count_nonzero(abs(roots(a))>1)>0:
            astab = mapinside(a)
        else:
            stable = True
        run = run + 1
        
    if count_nonzero(abs(roots(a))>1)>0:
        print "Caution: The algorithm did NOT result in a stable IIR filter!"
        print "Maybe try again with a higher value of tau0 or a higher filter order?"
        
    print "Least squares fit finished after %d iterations (tau=%d)." % (run,tau)
    Hd = freqz(b,a,2*pi*f/Fs)[1]
    Hd = Hd*exp(1j*2*pi*f/Fs*tau)
    res= hstack((real(Hd)-real(Hvals),imag(Hd)-imag(Hvals)))
    rms= sqrt( sum( res**2 )/len(f))
    print "Final rms error = %e \n\n" % rms

    return b,a,int(tau)    


def LSFIR(H,N,tau,f,Fs,Wt=None):
    """
    Least-squares fit of a digital FIR filter to a given frequency response.


    :param H: frequency response values
    :param N: FIR filter order
    :param tau: delay of filter
    :param f: frequencies
    :param Fs: sampling frequency of digital filter
    :param Wt: (optional) vector of weights

    :type H: ndarray
    :type N: int
    :type tau: int
    :type f: ndarray
    :type Fs: float

    :returns: filter coefficients bFIR (ndarray) of shape (N,)

    """
    import numpy as np

    print "\nLeast-squares fit of an order %d digital FIR filter to the" % N
    print "reciprocal of a frequency response given by %d values.\n" % len(H)

    H = H[:,np.np.newaxis]

    w = 2*np.np.pi*f/Fs
    w = w[:,np.np.newaxis]

    ords = np.np.arange(N+1)[:,np.np.newaxis]
    ords = ords.T

    E = np.np.exp(-1j*np.np.dot(w,ords))

    if not Wt == None:
        if len(np.shape(Wt))==2: # is matrix
            weights = np.np.diag(Wt)
        else:
            weights = np.eye(len(f))*Wt
        X = np.np.vstack([np.np.real(np.np.dot(weights,E)), np.np.imag(np.np.dot(weights,E))])
    else:
        X = np.np.vstack([np.np.real(E), np.np.imag(E)])

    H = H*np.np.exp(1j*w*tau)
    iRI = np.np.vstack([np.np.real(1.0/H), np.np.imag(1.0/H)])

    bFIR, res = np.linalg.lstsq(X,iRI)[:2]

    if not isinstance(res,np.ndarray):
        print "Calculation of FIR filter coefficients finished with residual norm %e" % res

    return np.reshape(bFIR,(N+1,))

