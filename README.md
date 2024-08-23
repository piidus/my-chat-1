# A my-chat-1 Flet app

An example of a minimal Flet app.

To run the app:

```bash
flet run [app_directory]
```

for details of apk
```bash
flet build apk --verbose > build_log.txt 2>&1
```
# To upgrade flutter

1. Navigate to the Flutter Directory
    Go to the directory where you previously downloaded and unzipped the Flutter SDK. For example:

```bash
cd /home/naru/development/flutter
```
2. Pull the Latest Changes
    Use the git pull command to fetch the latest changes from the Flutter repository:

```bash
git pull
```
3. Upgrade Flutter
    Once the latest changes are pulled, you can upgrade Flutter to the latest stable version by running:

```bash
flutter upgrade
```
This command will check for the latest stable version of Flutter, download it, and install it.

4. Verify the Upgrade
    After upgrading, you can verify the installed version of Flutter using:

```bash
flutter --version
```
This will display the current version of Flutter installed on your system.

5. Update PATH (if necessary)
    If you had set up the Flutter binary in your PATH, ensure it's still correctly set by checking:

```bash
echo $PATH
```
If the Flutter binary directory is not in your PATH, add it by editing your .bashrc or .zshrc file:

```bash
export PATH="$PATH:/home/naru/development/flutter/bin"
```
Then, apply the changes:

```bash
source ~/.bashrc  # or source ~/.zshrc
```
This will ensure that the Flutter command is available in your terminal.

# use p4a to apk
```bash
pip install python-for-android
pip install cython
```
2. install buildzer
```bash
pip install buildozer
```
```bash
buildozer init
```
-   add requiremts in build.spec
```bash
requirements = python3,kivy,flet,rsa,sqlalchemy
```
-   android.permissions: Add any necessary Android permissions (e.g., for internet access).
```bash
android.permissions = INTERNET
```
3. Build the APK
```bash
buildozer -v android debug
```
```bash
buildozer -v android release
```
