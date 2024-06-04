Testing
=======

Since Pythagoras, we know that :math:`1+2=9`.

   asdf asdafaasdfsdf asdf asdf asdf

:math:`\underline{x}=[  x_{1}, ...,  x_{n}]^{T}`

Setjum :math:`b_y=-6b_x` inn og fáum:

.. math::
   9 = \sqrt{b_x^2+b_y^2}

Dæmi
~~~~

.. admonition:: Dæmi
    :class: daemi

    Fallið :math:`f(x) = \sqrt{x}`, :math:`f:[0,\infty[\to {{\mathbb  R}}`
    er diffranlegt á menginu :math:`]0,\infty[` og afleiðan er gefin með
    :math:`f'(x) = \frac 1{2\sqrt{x}} = \frac 12 x^{-1/2}` þar. Hins vegar
    er :math:`f` ekki diffranlegt í :math:`x=0` þrátt fyrir að fallgildið sé
    vel skilgreint (og fallið samfellt frá hægri) þar.

    Ef :math:`x>0` þá fæst

    .. math::

       \begin{aligned}
         \lim_{h\to 0} \frac{\sqrt{x+h}-\sqrt{x}}h &=
         \lim_{h\to 0} \frac{(\sqrt{x+h}-\sqrt{x})(\sqrt{x+h}+\sqrt{x})}{h(\sqrt{x+h}+\sqrt{x})}\\
         &= \lim_{h\to 0} \frac{\sqrt{x+h}^2-\sqrt{x}^2}{h(\sqrt{x+h}+\sqrt{x})}\\
         &= \lim_{h\to 0} \frac{x+h-x}{h(\sqrt{x+h}+\sqrt{x})}\\
         &= \lim_{h\to 0} \frac{1}{\sqrt{x+h}+\sqrt{x}} = \frac{1}{2\sqrt{x}},\end{aligned}

    sem segir okkur að :math:`f'(x) = \frac 12 x^{-1/2}`.

    Í vinstri endapunkti skilgreingarsvæðisins, :math:`x=0`, þá fæst hins
    vegar

    .. math::

       \begin{aligned}
         \lim_{h\to 0^+} \frac{\sqrt{h}-\sqrt{0}}h &=
         \lim_{h\to 0^+} \frac{\sqrt{h}}h\\
         &= \lim_{h\to 0^+} \frac{1}{\sqrt{h}} = \infty,\end{aligned}

    sem sýnir að fallið er ekki diffranlegt frá hægri í :math:`x=0`.

Reiknireglur
------------

Setning
~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`f` og :math:`g` vera föll sem eru diffranleg í punkti
    :math:`x`. Þá eru föllin :math:`f+g,\ f-g, kf` (þar sem :math:`k` er
    fasti) og :math:`fg` diffranleg í punktinum :math:`x`, og ef
    :math:`g(x)\neq 0` þá eru föllin :math:`1/g` og :math:`f/g` líka
    diffranleg í :math:`x`.

    Eftirfarandi formúlur gilda um afleiður fallanna sem talin eru upp hér
    að framan:

    (i)   :math:`(f+g)'(x)=f'(x)+g'(x)`
    (ii)  :math:`(f-g)'(x)=f'(x)-g'(x)`
    (iii) :math:`(kf)'(x)=kf'(x)`, þar sem :math:`k` er fasti
    (iv)  :math:`(fg)'(x)=f'(x)g(x)+f(x)g'(x)`
    (v)   :math:`\displaystyle\Bigg(\frac{1}{g}\Bigg)'(x)=\frac{-g'(x)}{g(x)^2}`,
          ef :math:`g(x)\neq 0`
    (vi)  :math:`\displaystyle\Bigg(\frac{f}{g}\Bigg)'(x)=
          \frac{f'(x)g(x)-f(x)g'(x)}{g(x)^2}`, ef :math:`g(x)\neq 0`

Nokkrar afleiður
~~~~~~~~~~~~~~~~

(i)   :math:`\frac{d}{dx} c =  \lim_{h\to 0} \frac{c-c}h = 0`

(ii)  :math:`\frac{d}{dx} x =  \lim_{h\to 0} \frac{x+h-x}h = 1`

(iii) :math:`\frac{d}{dx} x^2 = \lim_{h\to 0} \frac{x^2+2xh+h^2-x^2}h
      = \lim_{h\to 0} \frac{2xh + h^2}h = \lim_{h\to 0} 2x+h= 2x`

Setning
~~~~~~~

.. admonition:: Setning
    :class: setning

    .. math:: \frac{d}{dx} x^n = n x^{n-1}

.. admonition:: Sönnun
    :class: setning, dropdown

    Sýnum þetta með þrepun.Tilfellið :math:`n=1` er afgreitt hér að ofan
    (3.3.2 (2) Setning 3.3.2).
    Gerum ráð fyrir að niðurstaðan gildi fyrir :math:`n` og sýnum að þá
    gildi hún einnig fyrir :math:`n+1`,

    .. math::

       \frac{d}{dx} x^{n+1} = \frac{d}{dx} (x\cdot x^n) =
           \left(\frac{d}{dx} x\right) x^n + x\frac{d}{dx} x^n
           = x^n + x\,
           \underbrace{n\, x^{n-1}}_\text{þ.f.}
           = (n+1) x^n.

Afleiður margliða
~~~~~~~~~~~~~~~~~

Með því að nota setningarnar að ofan þá eigum við ekki í neinum
vandræðum með að diffra margliður. Setning 3.3.1 (i) segir
að við getum diffrað hvern lið fyrir sig, liður (iii) í sömu setningu
segir að við getum tekið fastana fram fyrir afleiðuna og loks segir
Setning 3.3.3 hvernig við diffrum :math:`x^n`.

Dæmi: Afleiða margliðu
~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Dæmi
    :class: daemi

    Finnum afleiðu margliðunnar :math:`p(x) = 4x^3-2x + 5`. Nú er

    .. math::

       \begin{aligned}
       \frac{d}{dx} p(x)
       &= \frac{d}{dx}4x^3 - \frac{d}{dx}2x + \frac{d}{dx}5 \\
       &= 4\frac{d}{dx}x^3 -2\frac{d}{dx}x + \frac{d}{dx}5 =
       4\cdot 3x^2 -2\cdot 1 + 0 = 12x^2-2\end{aligned}

Setning: Keðjureglan
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Keðjureglan
    :class: setning

    Gerum ráð fyrir að :math:`f` og :math:`g` séu föll þannig að :math:`g`
    er diffranlegt í :math:`x` og :math:`f` er diffranlegt í :math:`g(x)`.
    Þá er samskeytingin :math:`f\circ g` diffranleg í :math:`x` og

    .. math:: (f\circ g)'(x) = f'(g(x))\cdot g'(x).

Dæmi
~~~~

.. admonition:: Dæmi
    :class: daemi

    Skoðum föllin :math:`f(x) = \sqrt x` og :math:`g(x) = 3x^5`. Bæði þessi föll eru
    diffranleg og afleiðurnar eru :math:`f'(x) = \frac 12 x^{-1/2}` og
    :math:`g'(x) = 15x^4`. Afleiða samskeytingarinnar :math:`f\circ g` er þá
    samkvæmt keðjureglunni

    .. math::
            (f\circ g)'(x) = \frac 12 (3x^5)^{-1/2} \cdot 15x^4.

--------


Hærri afleiður
--------------

Skilgreining
~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`f` vera fall. *Afleiðan* :math:`f'` er fall sem skilgreint er
    í öllum punktum þar sem :math:`f` er diffranlegt.

    Ef fallið :math:`f'` er diffranlegt í punkti :math:`x` þá er afleiða
    :math:`f'` í punktinum :math:`x` táknuð með :math:`f''(x)` og kölluð
    önnur afleiða (e. second derivative) :math:`f` í punktinum :math:`x`. Líta má á aðra afleiðu
    :math:`f` sem fall :math:`f''` sem er skilgreint í öllum punktum þar sem
    :math:`f'` er diffranlegt.

    Almennt má skilgreina :math:`n`\ *-tu afleiðu* :math:`f`, táknaða með
    :math:`f^{(n)}`, þannig að í þeim punktum :math:`x` þar sem fallið
    :math:`f^{(n-1)}` er diffranlegt þá er
    :math:`f^{(n)}(x)=\frac{d}{dx}f^{(n-1)}(x)`.

Dæmi
~~~~

.. admonition:: Dæmi
    :class: daemi

    Ef :math:`f(x)  = 3x^2`, þá er

    .. math:: f'(x) = 3\frac{d}{dx}x^2 = 3\cdot 2x = 6x

    og

    .. math:: f''(x) = \frac{d}{dx} 6x = 6.

Ritháttur
~~~~~~~~~

Ritum :math:`y=f(x)`.

Þá má tákna fyrstu afleiðu :math:`f` með

.. math:: y'= f'(x)=\frac{d}{dx}f(x)=D_xf(x)\ =\ D_x y= \frac{dy}{dx},

aðra afleiðuna með

.. math::

   \begin{aligned}
   y'' &=
   f''(x)=\frac{d}{dx}f'(x)=\frac{d}{dx}\frac{d}{dx}f(x)
   = D^2_xf(x)= D^2_x y=\frac{d^2}{dx^2}f(x)=\frac{d^2 y}{dx^2}\end{aligned}

og almennt :math:`n`-tu afleiðuna

.. math::

   \begin{aligned}
   y^{(n)} &= f^{(n)}(x)=\frac{d}{dx}f^{(n-1)}(x)=
   \frac{d}{dx}\Big(\frac{d^{n-1}}{dx^{n-1}}f(x)\Big) \\
   &=D^n_xf(x)\ =\ D^n_x y
   =\frac{d^n}{dx^n}f(x)
   = \frac{d^n y}{dx^n}.\end{aligned}

.. admonition:: Athugasemd
    :class: athugasemd

    Venja er að rita :math:`f'''` til að tákna þriðju afleiðu :math:`f` en
    afar sjaldgæft að :math:`f''''` sé notað til að tákna fjórðu afleiðu
    :math:`f` og mun algengara að nota :math:`f^{(4)}`.

------

Útgildi
-------

Skilgreining: Útgildi
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Við segjum að fall :math:`f` hafi staðbundið hágildi í punktinum
    :math:`x_0` ef til er bil :math:`(a,b)` umhverfis :math:`x_0`, sem er
    þannig að

    .. math:: f(x) \leq f(x_0), \quad \text{ fyrir öll } x \in (a,b).

    Við segjum að fall :math:`f` hafi staðbundið lággildi í punktinum
    :math:`x_0` ef til er bil :math:`(a,b)` umhverfis :math:`x_0`, sem er
    þannig að

    .. math:: f(x) \geq f(x_0), \quad \text{ fyrir öll } x \in (a,b).

    Tölum um að fallið :math:`f` hafi staðbundið útgildi í punktinum
    :math:`x_0` ef það hefur staðbundið hágildi eða staðbundið lággildi þar.

Setning
~~~~~~~

.. admonition:: Setning
    :class: setning

    Ef fallið :math:`f` hefur staðbundið útgildi í punktinum :math:`x_0` og
    er diffranlegt þá er :math:`f'(x_0)=0`.

.. admonition:: Sönnun
    :class: setning, dropdown

    Gerum ráð fyrir að :math:`f` hafi staðbundið hágildi í punktinum :math:`x_0`.
    Þá er :math:`f(x_0)-f(x)\geq 0` og ef :math:`x<x_0`,
    þá fæst að  :math:`\frac{f(x_0)-f(x)}{x_0-x}\geq 0`. Þetta þýðir að

    .. math::

       \lim_{x \to x_0^-} = \frac{f(x_0) - f(x)}{x_0-x} \geq 0.

    Eins þá er :math:`f(x_0)-f(x)\geq 0` og ef :math:`x_0<x`,
    þá er :math:`\frac{f(x_0)-f(x)}{x_0-x} \leq 0`.
    Þetta þýðir að

    .. math::

       \lim_{x \to x_0^+} = \frac{f(x_0) - f(x)}{x_0-x} \leq 0.

    Við vitum að markgildið
    :math:`\lim_{x\to x_0} \frac{f(x_0)-f(x)}{x_0-x}` er til þar sem fallið
    er diffranlegt, það þýðir að markgildin frá hægri og vinstri eru þau
    sömu. Eina leiðin til þess að það samræmist hægri og vinstri markgildunum
    hér að ofan er ef

    .. math:: f'(x_0) = \lim_{x\to x_0} \frac{f(x_0)-f(x)}{x_0-x} = 0.

.. admonition:: Aðvörun
    :class: advorun

    Þó að :math:`f'(a)=0` þá er ekki víst að :math:`a` sé staðbundið útgildi.

    Til dæmis þá hefur fallið :math:`f(x) = x^3` ekkert staðbundið útgildi
    þrátt fyrir að :math:`f'(0) = 0` (:math:`f'(x) = 3x^2`).

----------

Hornaföll og afleiður þeirra
----------------------------

Setning
~~~~~~~

.. admonition:: Setning
    :class: setning

    (i)   :math:`\displaystyle\lim_{x\rightarrow 0}\frac{\sin x}{x}=1`
    (ii)  :math:`\displaystyle\lim_{x\rightarrow 0}\frac{\cos x-1}{x}=0`
    (iii) :math:`\displaystyle\frac{d}{dx}\sin x=\cos x`
    (iv)  :math:`\displaystyle\frac{d}{dx}\cos x=-\sin x`
    (v)   :math:`\displaystyle\frac{d}{dx}\tan x=\frac{1}{\cos^2 x}=1+\tan^2 x`

--------

Meðalgildissetningin
--------------------

Setning Rolle
~~~~~~~~~~~~~

.. admonition:: Setning Rolle
    :class: setning

    Látum :math:`g:[a,b]\rightarrow{{\mathbb  R}}` vera samfellt fall. Gerum
    ráð fyrir að :math:`g` sé diffranlegt í öllum punktum í bilinu
    :math:`(a,b)`. Ef :math:`g(a)=g(b)` þá er til punktur :math:`c` á bilinu
    :math:`(a,b)` þannig að :math:`g'(c)=0`.

.. admonition:: Sönnun
    :class: setning, dropdown

    Ef :math:`g(x)=c` er fasti, þá er :math:`g'(x)=0`. Ef hins vegar
    :math:`g` er ekki fasti þá er til :math:`x \in (a,b)` þannig að
    :math:`g(x)\neq g(a)`, gerum ráð fyrir að :math:`g(x)>g(a)`
    (tilfellið ef :math:`g(x)<g(a)` gengur nánast eins fyrir sig).
    Samkvæmt há- og lággildislögmálinu
    þá tekur fallið :math:`g` sitt hæsta
    gildi í punkti :math:`c` á bilinu :math:`[a,b]`.Þar sem
    :math:`g(c)\geq g(x) >  g(a) = g(b)` þá getur :math:`c` hvorki verið
    :math:`a` né :math:`b`.
    Þar sem :math:`c`
    er útgildi þá segir Setning 3.5.2 að :math:`g'(c)=0`.

Meðalgildissetningin
~~~~~~~~~~~~~~~~~~~~

.. admonition:: Meðalgildissetningin
    :class: setning

    Látum :math:`f:[a,b]\rightarrow{{\mathbb  R}}` vera samfellt fall. Gerum
    ráð fyrir að :math:`f` sé diffranlegt í öllum punktum í bilinu
    :math:`(a,b)`. Þá er til punktur :math:`c` í bilinu :math:`(a,b)` þannig
    að

    .. math:: \frac{f(b)-f(a)}{b-a}=f'(c).

.. admonition:: Sönnun
    :class: setning, dropdown

    Skilgreinum nýtt fall

    .. math:: h(x)=f(x)-\left(f(a)+ \frac{f(b)-f(a)}{b-a}(x-a)\right).

    Athugið að :math:`h` er bara :math:`f` mínus línufallið gegnum punktana
    :math:`(a,f(a))` og :math:`(b,f(b))`. Þetta þýðir að :math:`h` er diffranlegt
    og að :math:`h(a)=h(b)=0`. Þá gefur Setning Rolle að til er :math:`c` þannig að
    :math:`h'(c)=0`.

    Nú er

    .. math::
    	h'(x) = f'(x) - \left(0+\frac{f(b)-f(a)}{b-a}(1-0)\right)
    	= f'(x) - \frac{f(b)-f(a)}{b-a}

    þannig að

    .. math:: 0 = h'(c) = f'(c) - \frac{f(b)-f(a)}{b-a},

    eða

    .. math:: f'(c) = \frac{f(b)-f(a)}{b-a}.

.. admonition:: Athugasemd
    :class: athugasemd

    Niðurstöðuna úr meðalgildissetningunni má orða svona:

    Í einhverjum punkti á bilinu er stundarbreytingin jöfn meðalbreytingunni
    yfir allt bilið.

Alhæfða meðalgildissetningin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Setning
    :class: setning

    Gerum ráð fyrir að föllin :math:`f` og :math:`g` séu samfelld á lokaða
    bilinu :math:`[a,b]` og diffranleg á opna bilinu :math:`(a,b)`. Gerum
    auk þess ráð fyrir að fyrir allar tölur :math:`x` í :math:`(a,b)` sé
    :math:`g'(x)\neq 0`. Þá er til tala :math:`c\in (a,b)` þannig að

    .. math:: \frac{f(b)-f(a)}{g(b)-g(a)}=\frac{f'(c)}{g'(c)}.

----------

Vaxandi og minnkandi föll
-------------------------

Skilgreining: Vaxandi/minnkandi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Fall :math:`f` er *vaxandi* á bili :math:`(a,b)` ef um
    alla punkta :math:`x_1` og :math:`x_2` á :math:`(a,b)` þannig að
    :math:`x_1 < x_2` gildir að

    .. math:: f(x_1) \leq f(x_2).

    Fall :math:`f` er *stranglega vaxandi* á bili :math:`(a,b)`
    ef um alla punkta :math:`x_1` og :math:`x_2` á :math:`(a,b)` þannig að
    :math:`x_1 < x_2` gildir að

    .. math:: f(x_1) < f(x_2).

    Fall :math:`f` er *minnkandi* á bili :math:`(a,b)` ef um
    alla punkta :math:`x_1` og :math:`x_2` á :math:`(a,b)` þannig að
    :math:`x_1 < x_2` gildir að

    .. math:: f(x_1) \geq f(x_2).

    Fall :math:`f` er *stranglega minnkandi* á bili
    :math:`(a,b)` ef um alla punkta :math:`x_1` og :math:`x_2` á
    :math:`(a,b)` þannig að :math:`x_1 < x_2` gildir að

    .. math:: f(x_1) > f(x_2).

.. admonition:: Athugasemd
    :class: athugasemd

    Kennslubókin notar *nondecreasing/nonincreasing* fyrir vaxandi/minnkandi og
    *increasing/decreasing* fyrir stranglega vaxandi/minnkandi.

    Einnig þekkist að nota *increasing/decreasing* og *strictly increasing/decreasing*.
    Til dæmis er það gert á `Wikipedia: Monotonic functions <https://en.wikipedia.org/wiki/Monotonic_function>`_.

Setning
~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`f` vera diffranlegt fall á bili. Þá er :math:`f` vaxandi þá og því
    aðeins að :math:`f' \geq 0`.

.. admonition:: Sönnun
    :class: setning, dropdown

    Byrjum á að gera ráð fyrir að fallið sé vaxandi. Festum punkt :math:`x` og
    sýnum að :math:`f'(x)\geq 0`. Þar sem :math:`f` er vaxandi þá gildir fyrir
    sérhvert :math:`h>0` að

    .. math::
        \frac{f(x+h)-f(x)}{h} \geq 0

    Þá gildir einnig um markgildið :math:`\lim_{h\to 0^+} \frac{f(x+h)-f(x)}h \geq 0`.

    Ef hins vegar :math:`h<0` þá er :math:`x+h < x` og því
    :math:`f(x+h)<f(x)`. Þetta gefur að

    .. math::
        \frac{f(x+h)-f(x)}h \geq 0

    sem þýðir að :math:`\lim_{h\to 0^-} \frac{f(x+h)-f(x)}h \geq 0`. Og þar af leiðandi
    er :math:`f'(x) = \lim_{h\to 0} \frac{f(x+h)-f(x)}h \geq 0`.

    Gerum nú ráð fyrir :math:`f'\geq 0` og sýnum að þá sé fallið vaxandi.
    Festum tvo punkta :math:`x_1 < x_2`. Ef :math:`f(x_1) > f(x_2)`, það er
    :math:`f(x_2)-f(x_1)<0`
    þá er

    .. math::
        \frac{f(x_2)-f(x_1)}{x_2-x_1} < 0.

    Samkvæmt meðalgildissetningunni þá er til punktur á bilinu :math:`[x_1,x_2]`
    þar sem afleiðan tekur þetta gildi, en það er í mótsögn við að  :math:`f'(c)\geq 0`.


Setning
~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`f` vera diffranlegt fall á bili. Þá er :math:`f` minnkandi þá og
    því aðeins að :math:`f' \leq 0`.

Setning
~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`f` vera diffranlegt fall á bili. Ef :math:`f'>0` þá er :math:`f`
    stranglega vaxandi.

Setning
~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`f` vera diffranlegt fall á bili. Ef :math:`f'<0` þá er :math:`f`
    stranglega minnkandi.

.. admonition:: Aðvörun
    :class: advorun

    Diffranlegt fall getur verið stranglega vaxandi/minnkandi án þess að
    afleiðan sé alls staðar stærri/minni en 0. Til dæmis er afleiða :math:`f(x)=x^3` jöfn 0 í
    :math:`x=0` en fallið er stranglega vaxandi á öllum rauntalnaásnum.

Afleiður fastafalla
~~~~~~~~~~~~~~~~~~~

Við vitum að ef :math:`f` er fasti, það er :math:`f(x)=c`, þá er
:math:`f'(x)=0` fyrir öll :math:`x`.

Nú fáum við einnig eftirfarandi út frá Setningum 3.8.2 og 3.8.3:

Ef :math:`f` er diffranlegt fall á bili :math:`I` sem er þannig að
:math:`f'(x) = 0` á :math:`I`, þá er :math:`f` fasti,
þ.e. \ :math:`f(x) = c` fyrir öll :math:`x\in I`.

Innsetning
~~~~~~~~~~

Ef við viljum reikna :math:`\int f(g(x))g'(x)\, dx` þá dugar okkur að
geta fundið :math:`\int f(x)\, dx`.

Notkun á innsetningu
~~~~~~~~~~~~~~~~~~~~

Setjum :math:`u=g(x)`. Þá er

.. math:: \frac{du}{dx}=g'(x)\qquad \text{eða} \qquad du=g'(x)\,dx.

Svo

.. math::

   \underbrace{\int f(g(x))g'(x)\,dx}_{\text{Viljum finna}}  =
   \int f(u)\,du
   =
   \underbrace{F(u)+C}_{\text{Getum reiknað}}  =
   \underbrace{F(g(x))+C}_{\text{Svarið}}.

.. admonition:: Aðvörun
    :class: advorun

    Ef við breytum heildi með tilliti til :math:`x` í heildi með tilliti til
    annarar breytistærðar :math:`u` þá verða **öll** :math:`x` að hverfa úr
    heildinu við breytinguna.

Notkun á innsetningu með mörkum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Með mörkum þá verður innsetningin svona

.. math::

   \begin{aligned}
     \int_a^b f(g(x))g'(x)\, dx  &=&
     \int_{x=a}^{x=b} f(u)\, du  =
     [F(u)]_{x=a}^{x=b}    \\ &=&
     [F(g(x))]_{x=a}^{x=b}     =
     F(g(b)) - F(g(a)).\end{aligned}

Ef :math:`A=g(a)` og :math:`B=g(b)` þá getum við eins skrifað þetta
svona

.. math::

   \begin{aligned}
   \int_a^b f(g(x))g'(x)\, dx  &=&
   \int_{x=a}^{x=b} f(u)\, du  =
   \int_{A}^{B} f(u)\, du    \\ &=&
   [F(u)]_A^B      =
   F(B) - F(A).\end{aligned}

Öfug innsetning
~~~~~~~~~~~~~~~

Reiknum :math:`\int f(x)\, dx`, með því að finna hugsanlega flóknara
heildi sem við getum reiknað

.. math::
    \int f(g(u))g'(u)\, du.

.. admonition:: Aðvörun
    :class: advorun

    Athugið að hér þurfum við að finna heppilegt :math:`g`. Það
    er ekki alltaf augljóst hvaða :math:`g` er hægt að nota.

Notkun á öfugri innsetningu
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setjum :math:`x=g(u)`. Þá er

.. math:: \frac{dx}{du}=g'(u)\qquad\quad dx=g'(u)\,du.

Sem gefur að

.. math::

   \underbrace{\int f(x)\,dx}_{\text{Viljum finna}}  =
   \int f(g(u))g'(u)\,du
   =
   \underbrace{F(u) + C}_{\text{Getum reiknað}}
   = \underbrace{F(g^{-1}(x)) + C}_{\text{Svarið}}.

Öfug innsetning með mörkum
~~~~~~~~~~~~~~~~~~~~~~~~~~

Við öfuga innsetningu þarf að passa að breyta mörkunum. Það er

.. math::

   \begin{aligned}
   \int_a^b f(x)\,dx    &= \int_{x=a}^{x=b} f(g(u))g'(u)\,du  \\
   &= [F(u)]_{x=a}^{x=b} = [F(g^{-1}(x))]_a^b = F(g^{-1}(b)) - F(g^{-1}(a)).\end{aligned}

Eða ef :math:`a=g(A)` og :math:`b=g(B)` (það er :math:`g^{-1}(a) = A` og
:math:`g^{-1}(b) = B`),

.. math:: \int_a^b f(x)\,dx  = \int_A^B f(g(u))g'(u)\,du= [F(u)]_A^B = F(B) - F(A).

Hlutheildun
~~~~~~~~~~~

Munum að ef :math:`u` og :math:`v` eru föll þá er
:math:`(u\cdot v)' = u'\cdot v + u \cdot v'`.

Notum Undirstöðusetningu stærðfræðigreiningarinnar og heildum beggja
vegna jafnaðarmerkisins, þá fæst

.. math:: u(x)v(x) = \int (u(x)v(x))'\, dx = \int u'(x)v(x)\, dx + \int u(x)v'(x)\, dx.

Það er

.. math:: \int u'(x)v(x)\, dx = u(x)v(x) -  \int u(x)v'(x)\, dx.

Hlutheildun með mörkum
~~~~~~~~~~~~~~~~~~~~~~

Eða með mörkum

.. math:: \int_a^b u'(x)v(x)\, dx = [u(x)v(x)]_a^b -  \int_a^b u(x)v'(x)\, dx.

(Athugið að þá verða engin :math:`x` í svarinu.)

Stofnbrotaliðun
~~~~~~~~~~~~~~~


Ef við viljum heilda rætt fall :math:`\frac{P(x)}{Q(x)}` þar sem :math:`P(x)`
og :math:`Q(x)` eru margliður, getur það reynst þrautinni þyngra, séu margliðurnar
nægilega flóknar. Stofnbrotaliðun gengur út á það að skrifa ræða fallið
:math:`\frac{P(x)}{Q(x)}` sem línulega samantekt liða á forminu

.. math:: \frac{1}{ax+b}, \quad \frac{x}{x^2+bx+c} \quad\text{ og }\quad \frac{1}{x^2+bx+c},

(það er við liðum fallið í stofnbrot sín) því svona liði getum við heildað hvern fyrir sig.

Erfitt er að setja aðferðina **stofnbrotaliðun** fram með einföldum hætti
og er það líkast til best gert með dæmum. Lítum á  nokkrar mismunandi útfærslur
af því hvernig hægt er að liða rætt fall í stofnbrot.

Athugum að margliða :math:`p(x)` er sögð af stigi :math:`n \in \mathbb{N}` ef hana má rita á forminu

.. math:: a_n x^n + a_{n-1} x^{n-1}+ \dots + a_1 x + a_0.

Ef hana má þátta í

.. math:: p(x) = (x-a_1)(x-a_2) \cdot \dots \cdot (x-a_q)

er hún sögð hafa einfaldar núllstöðvar ef um sérhverja núllstöð hennar :math:`a_i` og :math:`a_j` gildir
að :math:`a_i \neq a_j` fyrir öll :math:`i \neq j`. Ef, á hinn bóginn, til eru tvær eða fleiri núllstöðvar sem uppfylla að
:math:`a_i = a_j` þar sem :math:`i \neq j` þá eru þær kallaðar margfaldar núllstöðvar.

Sem dæmi má taka að margliðuna :math:`p(x)=x^2-2x+1` má þátta með samokareglunni í :math:`p(x)=(x-1)(x-1)`
og hefur hún því eina, tvöfalda núllstöð í :math:`x=1`. Hins vegar má þátta margliðuna :math:`q(x)=x^2+5x+6`
í :math:`q(x)=(x+2)(x+3)` og hefur hún því tvær einfaldar núllstöðvar, :math:`x=-2` og :math:`x=-3`.

Dæmi 1 um stofnbrotaliðun
~~~~~~~~~~~~~~~~~~~~~~~~~

Í þessu dæmi er teljarinn er af stigi :math:`m` og nefnarinn af stigi :math:`n>m` með :math:`n` einfaldar núllstöðvar.

.. admonition:: Dæmi
    :class: daemi

    Liðið :math:`\frac{x+4}{x^2-5x+6}` í stofnbrot.

.. admonition:: Lausn
    :class: daemi, dropdown

    Sjá má að teljarinn er margliða af fyrsta stigi
    en nefnarinn margliða af öðru stigi. Jafnframt má þátta nefnarann í :math:`(x-2)(x-3)`
    sem segir okkur að nefnarinn hefur tvær einfaldar núllstöðvar í :math:`x=2` og :math:`x=3`.
    Þá gildir að

    .. math:: \frac{x+4}{x^2-5x+6} = \frac{x+4}{(x-2)(x-3)} = \frac{A}{x-2}+\frac{B}{x-3},

    þar sem sem :math:`A` og :math:`B` eru einhverjar rauntölur. Tökum sérstaklega eftir því
    að fjöldi liða í stofnbrotaliðuninni er jafn stigi nefnarans. Ef :math:`P(x)` er margliða
    af stigi :math:`m` og :math:`Q(x)` er margliða af stigi stigi :math:`n>m` sem hefur
    :math:`n` mismunandi (raungildar) núllstöðvar, sem og að stuðullinn fyrir framan
    :math:`x^n` er :math:`1`, þá gildir almennt fyrir ræða fallið :math:`\frac{P(x)}{Q(x)}` að
    stofnbrotaliðun þess verður

    .. math:: \frac{P(x)}{Q(x)} = \frac{A_1}{x-a_1}+\frac{A_2}{x-a_2}+\dots +\frac{A_n}{x-a_n}.

    Ákvörðum nú gildi fastanna :math:`A` og :math:`B`. Samnefnum brotin í hægri
    hlið jöfnunnar

    .. math:: \frac{x+4}{x^2-5x+6} = \frac{A}{x-2}+\frac{B}{x-3} = \frac{Ax-3A+Bx-2B}{(x-2)(x-3)}.

    Með því að bera saman teljara brotanna, sem staðsett eru sitt hvoru megin jafnaðarmerkisins,
    sjáum við að

    .. math:: x+4 = Ax-3A+Bx-2B.

    Athugum að til þess að þetta sé jafngilt verður að gilda að :math:`Ax+Bx = x` og :math:`-3A-2B=4`.
    Með því að deila í gegnum fyrri jöfnuna með :math:`x` fæst jöfnuhneppið

    .. math::
    	\begin{aligned}
    		A+B&=1\\
    		-3A-2B&=4\\
    	\end{aligned}

    sem hefur lausnina :math:`A=-6` og :math:`B=7`. Af þessu sést að

    .. math::  \frac{x+4}{x^2-5x+6} = -\frac{6}{x-2}+\frac{7}{x-3}.

Dæmi 2 um stofnbrotaliðun
~~~~~~~~~~~~~~~~~~~~~~~~~

Í þessu dæmi eru teljarinn og nefnarinn af stigi :math:`n` og nefnarinn með :math:`n` einfaldar núllstöðvar.

.. admonition:: Dæmi
    :class: daemi

    Liðið :math:`\frac{x^3+2}{x^3-x}` í stofnbrot.

.. admonition:: Lausn
    :class: daemi, dropdown

    Sjá má að bæði teljari og nefnari eru margliður
    af þriðja stigi. Athugum að með því að bæta núlllið á forminu :math:`+x-x` við teljarann fæst


    .. math:: \frac{x^3-x+x+2}{x^3-x} = \frac{x^3-x}{x^3-x} + \frac{x+2}{x^3-x} = 1 + \frac{x+2}{x^3-x}.

    Fastann 1 þarf ekki að liða frekar. Þar sem að brotið :math:`\frac{x+2}{x^3-x}` hefur teljara af
    lægra stigi en nefnarinn (tveimur lægra nánar til tekið) sem og að nefnarinn hefur þrjár, einfaldar núllstöðvar,
    getum við stofbrotaliðað það með eftirfarandi hætti.

    .. math:: \frac{x+2}{x^3-x} = \frac{x+2}{x(x-1)(x+1)} = \frac{A}{x}+\frac{B}{x-1}+\frac{C}{x+1} = \frac{A(x^2-1)+B(x^2+x)+C(x^2-x)}{x(x-1)(x+1)}

    þar sem síðasti liður jöfnunnar fæst með því að samnefna brot þess næstseinasta.
    Með því að bera saman teljara fyrsta og síðasta liðs jöfnunnar sést að

    .. math:: x+2 = A(x^2-1) + B(x^2+x)+C(x^2-x).

    Ef við margföldum upp úr svigum og drögum saman líka liði fæst að

    .. math:: x+2 = (A+B+C)x^2 +(B-C)x - A.

    Þetta gefur okkur jöfnuhneppið

    .. math::
    	\begin{aligned}
    		A+B+C &= 0\\
    		B-C &=1\\
    		-A &= 2\\
    	\end{aligned}

    sem hefur lausnina :math:`A=-2`, :math:`B=\frac{3}{2}` og :math:`C=\frac{1}{2}`.
    Af þessu sést að

    .. math:: \frac{x^3+2}{x^3-x} = 1 - \frac{2}{x}+\frac{3}{2(x-1)}+\frac{1}{2(x-1)}.

Dæmi 3 um stofnbrotaliðun
~~~~~~~~~~~~~~~~~~~~~~~~~

Í þessu dæmi er teljarinn af stigi :math:`m` og nefnarinn af stigi :math:`n>m` stigi með :math:`r<n` einfaldar núllstöðvar.

.. admonition:: Dæmi
    :class: daemi

    Liðið :math:`\frac{x^2+3x+2}{x(x^2+1)}` í stofnbrot.

.. admonition:: Lausn
    :class: daemi, dropdown

    Athugum að teljarinn er
    annars stigs margliða en nefnarinn margliða af þriðja stigi. Hér þarf að gæta
    sérstaklega að því að nefnarinn hefur þó einungis eina, einfalda núllstöð
    í :math:`x=0` þar sem að þátturinn :math:`x^2+1` hefur engar (raungildar)
    núllstöðvar. Af þessu leiðir að :math:`\frac{x^2+3x+2}{x(x^2+1)}` má liða í
    stofnbrot á eftirfarandi vegu.

    .. math:: \frac{x^2+3x+2}{x(x^2+1)} = \frac{A}{x}+\frac{Bx+C}{x^2+1} = \frac{A(x^2+1)+Bx^2+Cx}{x(x^2+1)}

    Með svipuðum hætti og áður berum við saman teljara fyrsta brots og síðasta
    brots jöfnunnar. Sjáum að

    .. math:: x^2+3x+2 = A(x^2+1)+Bx^2+Cx.

    Með því að leysa upp úr svigum og draga saman líka liði fæst að


    .. math:: x^2+3x+2 = (A+B)x^2+Cx+A.

    Þetta gefur okkur jöfnuhneppið

    .. math::
    	\begin{aligned}
    		A+B &= 1\\
    		C &=3\\
    		A &= 2\\
    	\end{aligned}

    sem hefur lausnina :math:`A=2`, :math:`B=-1` og :math:`C=3`. Af þessu sést að

    .. math:: \frac{x^2+3x+2}{x(x^2+1)} = \frac{2}{x} + \frac{-x+3}{x^2+1}.

Dæmi 4 um stofnbrotaliðun
~~~~~~~~~~~~~~~~~~~~~~~~~

Í þessu dæmi er teljarinn af stigi :math:`m` og nefnari af stigi :math:`n>m` stigi með :math:`n` núllstöðvar, þar af einhverjar fjölfaldar.

.. admonition:: Dæmi
    :class: daemi

    Liðið :math:`\frac{1}{x(x-1)^2}` í stofnbrot.

.. admonition:: Lausn
    :class: daemi, dropdown

    Ljóst er að teljari er af hærra stigi
    en nefnarinn og nefnarinn hefur einfalda núllstöð í :math:`x=0` og tvöfalda
    núllstöð í :math:`x=1`. Þá má liða fallið í stofnbrot með eftirfarandi hætti.

    .. math:: \frac{1}{x(x-1)^2} = \frac{A}{x} + \frac{B}{x-1} + \frac{C}{(x-1)^2}.

    Tökum sérstaklega eftir því að núllstöðin :math:`x=1` er tvöföld og því inniheldur
    stofnbrotaliðunin tvo liði með þáttinn :math:`(x-1)` í nefnara,
    annars vegar í fyrsta veldi og hins vegar í öðru veldi. Almennt gildir, fyrir
    sérhverja :math:`r`-falda núllstöð :math:`a` nefnara ræða fallsins
    :math:`\frac{P(x)}{Q(x)}`, að stofnbrotaliðun fallsins mun innihalda

    .. math:: \frac{A_1}{x-a}+\frac{A_2}{(x-a)^2}+\dots + \frac{A_r}{(x-a)^r}

    Með því að samnefna fáum við að

    .. math:: \frac{A}{x} + \frac{B}{x-1} + \frac{C}{(x-1)^2} = \frac{A(x^2-2x+1)+B(x^2-x)+Cx}{x(x-1)^2}.

    Með sambærilegum hætti og áður fæst að

    .. math:: 1 = A(x^2-2x+1)+B(x^2-x)+Cx

    og með því að leysa upp úr svigum og draga saman líka liði fæst

    .. math:: 1 = (A+B) x^2 + (-2A-B+C)x + A.

    Því fæst loks jöfnuhneppið

    .. math::
    	\begin{aligned}
    		A+B &= 0\\
    		-2A-B+C &=0\\
    		A &= 1\\
    	\end{aligned}

    sem hefur lausnina :math:`A=1`, :math:`B=-1` og :math:`C=1`. Af þessu sést að

    .. math:: \frac{1}{x(x-1)^2} = \frac{1}{x}-\frac{1}{x-1} + \frac{1}{(x-1)^2}

Dæmi 5 um stofnbrotaliðun
~~~~~~~~~~~~~~~~~~~~~~~~~

Í þessu dæmi er teljarinn af stigi :math:`m` og nefnarinn af stigi :math:`n>m` stigi með :math:`r<n` núllstöðvar og núllstöðvalausan þátt í veldinu :math:`q>1`.

.. admonition:: Dæmi
    :class: daemi

    Liðið í :math:`\frac{x^2+2}{4x^5+4x^3+x}` stofnbrot.

.. admonition:: Lausn
    :class: daemi, dropdown

    Hér er stig nefnara hærra en stig teljara
    og má þátta hann í :math:`x(2x^2+1)^2`. Nú er margliðan :math:`2x^2+1` núllstöðvalaus.
    Því má stofnbrotaliða fallið á eftirfarandi vegu.

    .. math:: \frac{x^2+2}{4x^5+4x^3+x} = \frac{A}{x}+\frac{Bx+C}{2x^2+1}+\frac{Dx+E}{(2x^2+1)^2}

    Líkt og áður skulum við veita því sérstakan gaum að þátturinn :math:`(2x^2+1)^2`
    er í öðru veldi og því hefur stofnbrotaliðunin tvo liði þar sem nefnarinn inniheldur
    margliðuna :math:`2x^2+1`, annars vegar í fyrsta veldi og svo hins vegar í öðru
    veldi. Sama almenna regla og áður gildir, ef nefnari fallsins inniheldur núllstöðvalausa
    margliðu :math:`p(x)^n` í nefnara, þar sem :math:`n` er einhver náttúruleg tala,
    þá mun stofnbrotaliðun fallsins innihalda liðina

    .. math:: \frac{A_k}{p(x)^k}, \qquad k=1,2,\dots,n.

    Ef við samnefnum brotin í hægri hlið jöfnunnar fæst

    .. math:: \frac{x^2+2}{4x^5+4x^3+x} = \frac{A(4x^4+4x^2+1)+B(2x^4+x^2)+C(2x^3+x)+Dx^2+Ex}{x(2x^2+1)^2}.

    Við getum nú borið saman teljarana og með því að leysa upp úr svigum og draga saman
    líka liði fæst

    .. math:: x^2+2 = (4A+2B)x^4 + 2Cx^3 + (4A+2B+D)x^2 + (C+E)x+A.

    Því fæst loks jöfnuhneppið

    .. math::
    	\begin{aligned}
    		4A+2B &= 0\\
    		2C &=0\\
    		4A+B+D &= 1\\
    		C+E &= 0\\
    		A &= 2\\
    	\end{aligned}

    sem hefur lausnina :math:`A=2`, :math:`B=-4`, :math:`C=0`, :math:`D=-3` og :math:`E=0`.
    Af þessu sést að

    .. math:: \frac{x^2+2}{4x^5+4x^3+x} = \frac{2}{x}-\frac{4x}{2x^2+1}-\frac{3x}{(2x^2+1)^2}.

Samantekt
~~~~~~~~~

Líkt og áður segir þá er stofnbrotaliðun notuð fyrir ræð föll sem erfitt getur
reynst að heilda í sínu upprunalega formi. Við stofnbrotaliðun er fallið liðað
í summu minni þátta og má þá heilda hvern þátt fyrir sig og leysa dæmið þannig
í fleiri en einfaldari skrefum.

Nánar er fjallað um stofnbrotaliðun í kafla 6.2 í kennslubókinni.

Sjá einnig `wikipedia síðuna um stofnbrotaliðun <https://en.wikipedia.org/wiki/Partial_fraction_decomposition#Example_3>`__.
Þar má t.a.m. sjá allar aðferðirnar, úr dæmunum hér að ofan, notaðar í einu og sama dæminu.

-----------

Óeiginleg heildi
----------------

Skilgreining: Óeiginleg heildi I
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`f` vera samfellt fall á bilinu :math:`[a, \infty)`.
    Skilgreinum

    .. math:: \int_a^\infty f(x)\,dx=\lim_{R\rightarrow\infty} \int_a^R f(x)\,dx.

    Fyrir fall :math:`f` sem er samfellt á bili :math:`(-\infty, b]`
    skilgreinum við

    .. math:: \int_{-\infty}^b f(x)\,dx=\lim_{R\rightarrow-\infty} \int_R^b f(x)\,dx.

    Heildi eins og þau hér að ofan kallast óeiginlegt heildi.

Í báðum tilvikum segjum við að óeiginlega heildið sé samleitið ef
markgildið er til, en ósamleitið ef markgildið er ekki til.

.. admonition:: Aðvörun
    :class: advorun

      Ef :math:`f` stefnir ekki á 0 þegar :math:`x\to \infty` þá
      er heildið ekki samleitið. En jafnvel þó fallið stefni á
      0 þá er ekki víst að heildið sé samleitið, samanber
      eftirfarandi dæmi.

Dæmi
~~~~

.. admonition:: Dæmi
    :class: daemi

    Heildið :math:`\int_1^\infty \frac{1}{x^p}\,dx` er samleitið ef
    :math:`p>1` en ósamleitið ef :math:`p\leq 1`.

    Ef :math:`p>1` þá er

    .. math:: \int_1^\infty \frac{1}{x^p}\,dx=\frac{1}{p-1}.

Skilgreining: Óeiginleg heildi I, framhald
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`f` vera fall sem er samfellt á öllum rauntalnaásnum.

    Heildi af gerðinni :math:`\int_{-\infty}^\infty f(x)\,dx` er sagt
    samleitið ef bæði heildin :math:`\int_{-\infty}^0 f(x)\,dx` og
    :math:`\int_0^\infty f(x)\,dx` eru samleitin og þá er

    .. math::

       \int_{-\infty}^\infty f(x)\,dx=\int_{-\infty}^0 f(x)\,dx +
         \int_0^\infty f(x)\,dx.

.. admonition:: Athugasemd
    :class: athugasemd

    Það skiptir ekki máli í hvaða punkti heildinu er skipt í tvennt, það má
    velja aðra tölu heldur en 0, útkoman verður alltaf sú sama.

Skilgreining: Óeiginleg heildi II
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`f` vera samfellt fall á bilinu :math:`(a, b]` og hugsanlega
    ótakmarkað í grennd við :math:`a`. Skilgreinum

    .. math:: \int_a^b f(x)\,dx=\lim_{c\rightarrow a^+} \int_c^b f(x)\,dx.

    Fyrir fall :math:`f` sem er samfellt á bili :math:`[a, b)` og hugsanlega
    ótakmarkað í grennd við :math:`b` þá skilgreinum við

    .. math:: \int_a^b f(x)\,dx=\lim_{c\rightarrow b^-} \int_a^c f(x)\,dx.

    Í báðum tilvikum segjum við að óeiginlega heildið sé samleitið ef
    markgildið er til en ósamleitið ef markgildið er ekki til.

Dæmi
~~~~

.. admonition:: Dæmi
    :class: daemi

    Heildið :math:`\int_0^1 \frac{1}{x^p}\,dx` er samleitið ef :math:`p<1`
    en ósamleitið ef :math:`p\geq 1`. Ef :math:`p<1` þá er

    .. math::

       \int_0^1
       \frac{1}{x^p}\,dx=\frac{1}{1-p}.

Skilgreining
~~~~~~~~~~~~

.. admonition:: Skilgreining
    :class: skilgreining

    Látum :math:`f` vera samfellt fall á bili :math:`(a,\infty)` og
    ótakmarkað í grennd við :math:`a`. Látum :math:`c` vera einhverja tölu
    þannig að :math:`a<c<\infty`.

    Heildið :math:`\int_a^\infty f(x)\,dx` er sagt vera samleitið ef bæði
    heildin :math:`\int_a^c f(x)\,dx` og :math:`\int_c^\infty f(x)\,dx` eru
    samleitin og þá er

    .. math:: \int_{a}^\infty f(x)\,dx=\int_{a}^c f(x)\,dx + \int_c^\infty f(x)\,dx.

.. admonition:: Athugasemd
    :class: athugasemd

    Það er sama hvað tala :math:`c` er valin hér að ofan, útkoman verður
    alltaf sú sama.

Setning
~~~~~~~

.. admonition:: Setning
    :class: setning

    Látum :math:`-\infty\leq a<b\leq \infty`. Gerum ráð fyrir að föllin
    :math:`f` og :math:`g` séu samfelld á :math:`(a, b)` og að um öll
    :math:`x\in (a, b)` gildi að :math:`0\leq f(x)\leq g(x)`.

    (i)  Ef heildið :math:`\int_a^b g(x)\,dx` er samleitið þá er heildið
         :math:`\int_a^b f(x)\,dx` líka samleitið og

         .. math:: \int_a^b f(x)\,dx \leq \int_a^b g(x)\,dx.

    (ii) Ef heildið :math:`\int_a^b f(x)\,dx` er ósamleitið þá er heildið
         :math:`\int_a^b g(x)\,dx` líka ósamleitið.