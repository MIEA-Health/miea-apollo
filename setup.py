from setuptools import setup, find_packages

install_requires = []
with open('requirements.txt') as requirements_txt:
    for requirement in requirements_txt:
        if str(requirement).startswith('git+'):
            git_url = requirement.split("+")[1]
            egg_name = requirement.split("egg=")[1].strip()
            repo_git_url = git_url.split(".git")[0] + '/tarball/master'
            requirement
            install_requires.append(f"{egg_name} @ {repo_git_url}")
        else:
            install_requires.append(str(requirement))

setup(
    name='apollo',
    version='0.0.1',
    description='Python based utility to standardize the collection of data for MIEA.',
    author='MIEA Data Engineering Team',
    author_email='tech@mieahealth.com',
    packages=find_packages(),
    install_requires=install_requires,
)
