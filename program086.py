def main(subject,verb,objects):
    for sub in subject:
        for ver in verb:
            for obj in objects:
                print("{0} {1} {2}".format(sub,ver,obj))
            
subject = input("Enter the subject : ").split(",")
verb = input("Enter the verb : ").split(",")
objects = input("Enter the object  : ").split(",")
main(subject=subject,verb=verb,objects=objects)