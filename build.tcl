#!/usr/bin/tclsh

set arch "x86_64"
set base "memcached-for-Tcl-1.2.1"

set var [list git clone https://github.com/bovine/memcached-for-Tcl.git $base]
exec >@stdout 2>@stderr {*}$var

set var2 [list tar czvf ${base}.tar.gz $base]
exec >@stdout 2>@stderr {*}$var2

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb memcached-for-Tcl_SUSE.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force $base
file delete -force $base.tar.gz

