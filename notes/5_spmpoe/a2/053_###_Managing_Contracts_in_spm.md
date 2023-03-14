 Here is the content in markdown format for the topic ### Managing Contracts in spm:

### Managing Contracts in spm

- SPM or Solidity Package Manager is used to manage contracts and libraries in a Solidity project.
- To install a contract or library, use `npm install <package-name> --save`. This will install the package and save it as a dependency in the package.json file.
- To update a contract or library, use `npm update <package-name>`. This will update the package to the latest version and update the package.json file with the new version number.
- To uninstall a contract or library, use `npm uninstall <package-name>`. This will remove the package and update the package.json file by removing the dependency.
- The package.json file holds information about the project and all its dependencies along with their version numbers. This file should always be committed to version control as it serves as an authoritative list of project dependencies.
- Dependencies in package.json can be specified with a version range using semantic versioning. This allows minor version updates to be installed automatically with `npm update`. Patch version updates are always installed automatically.
- To install all dependencies in one go when cloning a project, run `npm install`. This will read the package.json file and install all dependencies listed in it.
- SPM makes it easy to reuse contracts and libraries built by the community, thereby reducing duplication of work and encouraging modularity. It brings the rich package ecosystem of JavaScript to Solidity development.

Some mnemonics to remember:
- `npm install` to install, `npm update` to update, `npm uninstall` to uninstall
- Save dependencies with `--save` flag
- `package.json` is the source of truth for dependencies
- Use version ranges for dependencies to automatically install minor version updates

[Detailed diagrams and examples can be added here if required to aid learning]