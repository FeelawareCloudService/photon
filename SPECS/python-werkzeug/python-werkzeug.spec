%{!?python2_sitelib: %define python2_sitelib %(python2 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}
%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}

Summary:        The Swiss Army knife of Python web development
Name:           python-werkzeug
Version:        0.10.4
Release:        1%{?dist}
License:        BSD
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Url:            https://pypi.python.org/packages/source/W/Werkzeug/Werkzeug-%{version}.tar.gz
Source0:        Werkzeug-%{version}.tar.gz
%define         sha1 Werkzeug=bde8ef90a905ed52e0920493072d161a354a8fe1

BuildRequires:  python2
BuildRequires:  python2-libs
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-incremental

Requires:       python2
Requires:       python2-libs

BuildArch:      noarch

%description
Werkzeug started as simple collection of various utilities for WSGI applications and has become one of the most advanced WSGI utility modules. It includes a powerful debugger, full featured request and response objects, HTTP utilities to handle entity tags, cache control headers, HTTP dates, cookie handling, file uploads, a powerful URL routing system and a bunch of community contributed addon modules.

%package -n     python3-werkzeug
Summary:        python-werkzeug
BuildRequires:  python3-devel
BuildRequires:  python3-libs

Requires:       python3
Requires:       python3-libs
%description -n python3-werkzeug
Python 3 version.

%prep
%setup -q -n Werkzeug-%{version}
rm -rf ../p3dir
cp -a . ../p3dir

%build
python2 setup.py build
pushd ../p3dir
python3 setup.py build
popd

%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}
pushd ../p3dir
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
popd

%files
%defattr(-,root,root)
%{python2_sitelib}/*

%files -n python3-werkzeug
%defattr(-,root,root)
%{python3_sitelib}/*

%changelog
*   Tue Mar 14 2017 Xiaolin Li <xiaolinl@vmware.com> 0.10.4-1
-   Downgraded to 0.10.4.
*   Mon Mar 06 2017 Xiaolin Li <xiaolinl@vmware.com> 0.11.15-1
-   Initial packaging for Photon.
