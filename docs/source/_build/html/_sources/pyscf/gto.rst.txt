Molecule
========



.. py:class:: pyscf.gto()

    .. py:class:: pyscf.gto.mole()

        :param int verbose: Print level
        :param int spin: num. alpha electrons - num. beta electrons to control multiplicity. If spin = None is set, multiplicity will be guessed based on the neutral molecule.
        :param List atom: To define the molecular structure. Example:

        >>> from pyscf import gto
        >>> mol = gto.M(atom='H 0 0 0; F 0 0 1', basis='6-31g')
        >>> mol.atom
        >>> mol.elements
        >>> 'H 0 0 0; F 0 0 1'









