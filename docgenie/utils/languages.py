import re
import os

def __getRawImportsFromFile(file, file_extension):
    def getImportsFromPython(file):
        imports = []
        patterns = [
            r'import\s+([\w\.]+(?:\.[\w\.]+)*)',
            r'from\s+([\w\.]+(?:\.[\w\.]+)*)\s+import\s+[\w, \.]+'
        ]
        for line in file.split("\n"):
            for pattern in patterns:
                matches = re.findall(pattern, line)
                if matches:
                    for match in matches:
                        if type(match) == tuple:
                            imports.append(match[0])
                        else:
                            imports.append(match)
        return imports
    
    def getImportsFromJS(file):
        imports = []
        patterns = [
            r"\s*import\s+[\w\.\*]+\s+from\s+\"([\w\.\*\/*]+)\"",
            r"\s*import\s+[\w\.\*]+\s+from\s+\'([\w\.\*\/*]+)\'",
            r"\s*import\s+\'([\w\.\*\/*]+)\'",
            r"\s*import\s+\"([\w\.\*\/*]+)\"",
            r"\s*require\(\"([\w\.\*\/*]+)\"\)",
            r"\s*require\(\'([\w\.\*\/*]+)\'\)",
        ]
        for line in file.split("\n"):
            for pattern in patterns:
                matches = re.findall(pattern, line)
                if matches:
                    imports.extend(matches)
        return imports
    
    def getImportsFromTS(file):
        imports = []
        patterns = [
            r"\s*import\s+[\w\.\*]+\s+from\s+\"([\w\.\*\/*]+)\"",
            r"\s*import\s+[\w\.\*]+\s+from\s+\'([\w\.\*\/*]+)\'",
            r"\s*import\s+\'([\w\.\*\/*]+)\'",
            r"\s*import\s+\"([\w\.\*\/*]+)\"",
            r"\s*require\(\"([\w\.\*\/*]+)\"\)",
            r"\s*require\(\'([\w\.\*\/*]+)\'\)",
        ]
        for line in file.split("\n"):
            for pattern in patterns:
                matches = re.findall(pattern, line)
                if matches:
                    imports.extend(matches)
        return imports

    getImports = {
        ".py": getImportsFromPython,
        ".js": getImportsFromJS,
        ".ts": getImportsFromTS,
    }

    imports: list[str] = getImports[file_extension](file)
    return imports

def __getPossibleImports(file_path: str, file_extension: str):
    def modifyImportForPython(import_path: str):
        import_path = import_path.replace(".", "/")
        if import_path.startswith("//") or import_path.startswith("\\\\"):
            import_path = import_path.replace("//", "../")
        elif import_path.startswith("/"):
            import_path = import_path[1:]
        import_paths: list[str] = []
        if not import_path.endswith(".py"):
            import_paths.append(import_path.lower() + ".py")
            import_paths.append(import_path.lower() + "/__init__.py")
        else:
            import_paths.append(import_path.lower())
        return import_paths
    
    def modifyImportForJS(import_path: str):
        import_paths: list[str] = []
        if not import_path.endswith(".js") and not import_path.endswith(".ts"):
            import_paths.append(import_path.lower() + ".js")
            import_paths.append(import_path.lower() + "/index.js")
            import_paths.append(import_path.lower() + ".ts")
            import_paths.append(import_path.lower() + "/index.ts")
        else:
            import_paths.append(import_path.lower())
    
    def modifyImportForTS(import_path: str):
        import_paths: list[str] = []
        if not import_path.endswith(".js") and not import_path.endswith(".ts"):
            import_paths.append(import_path.lower() + ".js")
            import_paths.append(import_path.lower() + "/index.js")
            import_paths.append(import_path.lower() + ".ts")
            import_paths.append(import_path.lower() + "/index.ts")
        else:
            import_paths.append(import_path.lower())
    
    modifyImport = {
        ".py": modifyImportForPython,
        ".js": modifyImportForJS,
        ".ts": modifyImportForTS,
    }

    modified_imports = modifyImport[file_extension](file_path)
    return modified_imports

def getImportPathsFromCode(code: str, file_extension: str, src_dir: str):
    imports = __getRawImportsFromFile(code, file_extension)
    import_paths: list[str] = []

    for import_path in imports:
        possible_imports = __getPossibleImports(import_path, file_extension)
        for possible_import in possible_imports:
            # remove leading slash if present
            # bcz leading slash is used to indicate absolute path
            if possible_import.startswith("/") or possible_import.startswith("\\"):
                possible_import = possible_import[1:]

            path = os.path.join(src_dir, possible_import)
            if os.path.exists(path):
                import_paths.append(possible_import)
                break
    
    # make consistent
    import_paths = [path.replace("\\", "/") for path in import_paths]
    # remove duplicates
    import_paths = list(set(import_paths))
    return import_paths