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
#     spack install mpas
#
# You can edit this file again by typing:
#
#     spack edit mpas
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Mpas(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/MPAS-Dev/MPAS-Model/archive/refs/tags/v8.2.2.zip"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("8.2.2", sha256="9c07174e0addcead9242331d07e7bc78da7866f58d76b9b60f4f5abfe2807536")
    version("8.2.1", sha256="99d9ae0d17e93ecc4f196a3d655c8ab38d160145acccfbd4ce039f133223d89e")
    version("8.2.0", sha256="340420610353f9cd285641fc6fdac8e3155b1178476f606a26e57c93d4514d18")
    version("8.1.0", sha256="4e933756af41f0d7b6302737f8db7cfbc743ba38a7c8c5fb5a493176a49859fc")
    version("8.0.2", sha256="aea9444eda44e3a703d08937ad9248506ddc57ea32c83bd33cc6a4f41ced4037")
    version("8.0.1", sha256="b06bee6c579e2365f0456e3e128cba068d4a10a845659a76389316335e9c5787")
    version("8.0.0", sha256="5e80940e783669bfb818a119cbdf0f8e950e2aa7ec29f09a2237a059bd0c5265")
    version("7.3", sha256="d9123b68960acbf76eeea5cea77791f0789abcd138c002054345111f3a1a445b")
    version("7.2", sha256="d082d90b07d8a9ce1efe8b3b904e93248067483364d75f7b1804dae7bc476789")
    version("7.1", sha256="6311b114c0b2f32cfa0a4cf760ca00bd2079b81a903068209b998e3e9bd1c9a2")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    # FIXME: Add dependencies if required.
    # depends_on("foo")
    depends_on("mpi")
    depends_on("netcdf-c@4.4:^mpi")
    depends_on("netcdf-fortran")
    depends_on("parallel-netcdf@1.8:")
    depends_on("parallelio@1.71:")
    #
    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
