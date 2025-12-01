complaints = []

def submit(msg, cat):
    complaints.append({'id': len(complaints) + 1, 'msg': msg, 'cat': cat, 'status': 'pending'})
    print(f"\nSubmitted (ID: {len(complaints)})\n")

def view_all():
    if not complaints:
        print("\nNo complaints\n")
        return
    print("\n" + "="*50)
    for c in complaints:
        print(f"ID: {c['id']} | {c['cat']} | {c['status']}")
        print(f"Message: {c['msg']}")
        print("-"*50)
    print()

def by_category():
    if not complaints:
        print("\nNo complaints\n")
        return
    cats = {}
    for c in complaints:
        cat = c['cat']
        if cat not in cats:
            cats[cat] = []
        cats[cat].append(c)
    
    print()
    for cat in sorted(cats.keys()):
        print(f"{cat}: {len(cats[cat])} complaints")
    print()

def update(cid, status):
    for c in complaints:
        if c['id'] == cid:
            c['status'] = status
            print(f"\nUpdated\n")
            return
    print("\nNot found\n")

def delete(cid):
    for i, c in enumerate(complaints):
        if c['id'] == cid:
            complaints.pop(i)
            print("\nDeleted\n")
            return
    print("\nNot found\n")

def student_menu():
    cats = ["Academic", "Facilities", "Faculty", "Staff", "Admin", "Other"]
    print("\nCategories:")
    for i, c in enumerate(cats, 1):
        print(f"{i}. {c}")
    
    cat_choice = input("Select (1-6): ")
    if cat_choice in ['1', '2', '3', '4', '5', '6']:
        cat_idx = int(cat_choice) - 1
        msg = input("Your complaint: ")
        submit(msg, cats[cat_idx])
    else:
        print("Invalid selection\n")

def admin_menu():
    while True:
        print("\n1. View All  2. By Category  3. Update Status  4. Delete  5. Exit")
        ch = input("Choice: ")
        
        if ch == '1':
            view_all()
        elif ch == '2':
            by_category()
        elif ch == '3':
            cid_input = input("Complaint ID: ")
            if cid_input.isdigit():
                cid = int(cid_input)
                status = input("New status: ")
                update(cid, status)
            else:
                print("Invalid ID\n")
        elif ch == '4':
            cid_input = input("Complaint ID: ")
            if cid_input.isdigit():
                cid = int(cid_input)
                delete(cid)
            else:
                print("Invalid ID\n")
        elif ch == '5':
            break

def main():
    while True:
        print("\n" + "="*50)
        print("COMPLAINT BOX SYSTEM")
        print("="*50)
        print("1. Student - Submit Complaint")
        print("2. Admin - View Complaints")
        print("3. Exit")
        
        ch = input("\nChoice: ")
        
        if ch == '1':
            student_menu()
        elif ch == '2':
            admin_menu()
        elif ch == '3':
            print("\nGoodbye!\n")
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()