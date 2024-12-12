# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install crunchtope
#
# You can edit this file again by typing:
#
#     spack edit crunchtope
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Crunchtope(MakefilePackage):
    """
    CrunchTope: CrunchFlow is reactive transport software developed by Carl I. Steefel, Toshi Bandai, and Sergi Molins at Lawrence Berkeley National Laboratory.
    """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/CISteefel/CrunchTope"
    url = "https://github.com/CISteefel/CrunchTope/archive/refs/tags/v2.10.zip"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("2.10", sha256="498a7711b92f48f1e9d1e34f05a052a85d362b13f258e6baaf84bfb247b8ea1e")
    version("2.0.1", sha256="0b91a4893ddddb7bc6b4f91d0c9d2bf38537b92a8950b62243ac0786b112f364")
    version("2.0.0", sha256="2825538adea0e88ea3717bca2798b6a50438fae1faf80a9a1fb2057f5de25117")
    #
    parallel = False
    build_targets = ['ALL']
    #
    depends_on("fortran", type="build")
    #
    variant("lapack", values=bool, default=True,  description="Build with lapack.")
    variant("mpi",    values=bool, default=False, description="Build with MPI. Some features might not be MPI enabled.")
    variant("batch", values=bool, default=False, description="Build PETSC with +batch option, for srun MPI systems")
    #
    #Add dependencies if required.
    depends_on("petsc+batch", when="+batch")
    # TODO: better evaluate the PETSC requirement(s). Environment is currently configured with our standard,
    #   +batch +fftw +hwloc +libyaml +libpng +jpeg .
    #   +batch is required on Sherlock, to get around the `mpiexec` vs `srun` issue, but I am not sure what else we actually require.
    #   Also, maybe add some sort of +O {0,1,2,3} option for optimization?
    depends_on("petsc@3.21~mpi", when="~mpi")
    depends_on("petsc@3.21+mpi", when="+mpi")
    depends_on("blas", when="+lapack")
    depends_on("lapack", when="+lapack")
    #
    patch('df_210_makefile.patch', level=0, when="@2.10")
    #
    def edit(self, spec, prefix):
         #
         makefile = FileFilter("Makefile")
         makefile.filter("#chkopts", "")
         makefile.filter("chkopts", "")
         #
         #makefile.filter("FFLAGS ", "#FFLAGS") 
         #makefile.filter("${FFLAGS", "${FFLAGS} ${FF2}")
         #
         # a hack to provide working flags for gcc:
         if False and self.compiler.name == "gcc":
             #makefile.filter("FFLAGS  = -w -ffpe-trap=invalid,overflow,zero", "FFLAGS  = -Wall -fallow-argument-mismatch -Wno-lto-type-mismatch -w  -ffpe-trap=invalid,overflow,zero -ffree-line-length-none -Wno-unused-dummy-argument ")
             pass

    def install(self, spec, prefix):
        # https://spack.readthedocs.io/en/latest/build_systems/makefilepackage.html#variables-to-watch-out-for
        mkdir(prefix.bin)
        install("CrunchTope", prefix.bin)
        #install_tree("lib", prefix.lib)
    #
    def flag_handler(self, name, flags):
        #super().flag_handler(name,flags)
        #if name == "cxxflags":
        if name == 'fflags':
            # TODO: these are the FFLAGS from the makefile; we might refine our list:
            # FFLAGS  = -w -ffpe-trap=invalid,overflow,zero
            # -c -fPIC -fallow-argument-mismatch -w -Wall -Wno-lto-type-mismatch   -w -ffpe-trap=invalid,overflow,zero 
            flags.append('-fallow-argument-mismatch')
            flags.append('-Wall')
            flags.append('-Wno-lto-type-mismatch')
            flags.append('-w')
            for fl in [ '-ffpe-trap=invalid,overflow,zero', '-ffree-line-length-none', '-ffree-line-length-0', '-Wno-unused-dummy-argument']:
                flags.append(fl)
        #
        if name in ('cxxflags', 'fflags', 'cflags', 'ldflags'):
            flags.append(self.compiler.openmp_flag)
        return (flags, None, None)
        #return (None, flags, None)
    #
    def setup_build_environment(self, env):
        env.set("PETSC_DIR", self.spec["petsc"].prefix)
        #
        #env.set("FF2", "-Wall -fallow-argument-mismatch -Wno-lto-type-mismatch -w  -ffpe-trap=invalid,overflow,zero', '-ffree-line-length-none', '-ffree-line-length-0', '-Wno-unused-dummy-argument ")

