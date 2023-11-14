' Small script to remove tags from subtitles files
' Author : Vincent aka Lama
'
' To use this script, simply drag and drop the files onto
' the icon of the script. You can also do it from the command line
' by typing cscript RemoveTags.vbs <files>
' Of course this does only work in Windows (98 & later).
'
' The script makes a backup of the files processed, renamed with
' an .bak extension, and only process *.srt and *.sub files
' (you can change that, see below).
' Unless there is an error, there is no output!
'
' I'm in no way an expert in VBScript programming (it's pretty obvious
' from the programming style) and I don't want to be ;-). 
' This script is provided in the hope that it will be helpful to some,
' and comes with no warranty (backuping your data first is the way to go).


Dim Extensions          ' Extensions of the files to be processed
Dim FilesToProcess(64)  ' Files to be processed (MAX : 64 files)
Dim Patterns
Dim PatternsEmptyLine

' Here we only process .srt & .sub files. 
' To add more extensions, append "|\." and the extension
Extensions="\.srt|\.sub"

' Remove <i>, </i>, anything between { and }.
PatternsTags="(<i>)|(<\/i>)|({.*?})"
PatternsEmptyLine="<i>\s*<\/i>"

Set objArgs = WScript.Arguments

i = 0
j = 0

' See what file we need to process
Do While i <= WScript.Arguments.Count - 1
    arg = WScript.Arguments.Item(i)

    Set objRE = New RegExp
    objRE.IgnoreCase = True
    objRE.Pattern = Extensions

    Set Matches = objRE.Execute(arg)

    For Each Match In Matches
        If Match.firstIndex > 0 Then
            FilesToProcess(j) = arg
            REM Wscript.Echo Cstr(i) + " > " + arg
            j = j + 1
        End If
    Next

    i = i+ 1
Loop

' Make a backup (named after the filename + ".bak") 
For Each file in FilesToProcess
    If StrComp(file, "") <> 0 Then
        Set objInputFSO   = CreateObject("Scripting.FileSystemObject")
        objInputFSO.CopyFile file, file & ".bak"
        objInputFSO.DeleteFile file, True
    End If
Next

' Open the backup file and process it
Set reEmptyLine = New RegExp
reEmptyLine.Pattern = PatternsEmptyLine

Set reTags = New RegExp
reTags.Pattern = PatternsTags
reTags.Global  = True

For Each file in FilesToProcess
    If StrComp(file, "") <> 0 Then
        Set objInputFSO   = CreateObject("Scripting.FileSystemObject")
        Set objInputFile  = objInputFSO.OpenTextFile(file & ".bak")

        Set objOutputFSO  = CreateObject("Scripting.FileSystemObject")
        Set objOutputFile = objOutputFSO.CreateTextFile(file)

        Do While objInputFile.AtEndOfStream <> True
            inputLine = objInputFile.ReadLine

            If StrComp(inputLine, "") = 0 Then 
                objOutputFile.WriteLine(inputLine)
            Else
                outputLine = reEmptyLine.Replace(inputLine, "")
                If  StrComp(outputLine, "") <> 0 Then
                    outputLine = reTags.Replace(outputLine, "")
                    objOutputFile.WriteLine(outputLine)
                End If
            End If
        Loop
    End If
Next

