%define module	graphcanvas

Summary: 	Enthought Tool Suite - interactive graph visualization
Name: 	 	python-%{module}
Version: 	4.0.2
Release: 	1
Source0: 	https://www.enthought.com/repo/ets/graphcanvas-%{version}.tar.gz
License: 	BSD
Group: 	 	Development/Python
Url: 	 	https://github.com/enthought/graphcanvas/
BuildArch: 	noarch
Requires:  	python-enable >= 4.2.0
Requires:  	python-networkx
BuildRequires: 	python-setuptools >= 0.6c8
Obsoletes:  python-enthought-graphcanvas

%description
graphcanvas is an library for interacting with visualizations of
complex graphs. The aim is to allow the developer to declare the graph
by the simplest means and be able to visualize the graph immediately.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%files
%defattr(-,root,root)
%doc examples/ 
%py_sitedir/%{module}*


%changelog
* Mon Aug 13 2012 Lev Givon <lev@mandriva.org> 4.0.0-2
+ Revision: 814699
- Rebuild for ETS 4.2.0.

* Thu Jul 07 2011 Lev Givon <lev@mandriva.org> 4.0.0-1
+ Revision: 689185
- import python-graphcanvas



