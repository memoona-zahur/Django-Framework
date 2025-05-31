from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    peoples = [
        {"name": "Memoona", "age": 22},
        {"name": "Humna", "age": 16},
        {"name": "Imran", "age": 19},
        {"name": "Abdullah", "age": 12},
    ]

    # for people in peoples:
    #     if people['age'] > 10:
    #         print('Yes')

    vegetables = ["Potato", "Tomato", "Onion", "Carrot", "Cucumber"]

    text = """
           Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorem fugiat quod nesciunt quas consequuntur distinctio sunt quibusdam velit quam? Aspernatur eum similique deleniti voluptas, eaque id maxime a doloribus molestiae rerum rem voluptatibus molestias numquam consequatur quidem aut vero ullam ipsam expedita ab pariatur. Voluptatem in consequatur, eum nam sequi molestiae officia dicta tempore possimus ea ad expedita natus quisquam, minima earum. Delectus nam nisi error tempore, tenetur incidunt libero vel iste eveniet assumenda a magni deleniti fugiat laborum quam sunt odit sint molestias velit reprehenderit et culpa, quaerat at! Autem possimus nihil iure perspiciatis tenetur aspernatur, eius similique asperiores.
           """

    # for people in peoples:
    #     print(people)

    # return HttpResponse("""<h1>Hey I am a Django Server.</h1>
    #     <p>Hey this is coming from Django Server.</p>
    #     <hr>
    #     <h3 style="color:red">Hope you are loving it :) </h3>

    # """)

    return render(
        request,
        "home/index.html",
        context={
            "page": "Django Tutorial",
            "peoples": peoples,
            "text": text,
            "vegetables": vegetables,
        },
    )


def about(request):
    context = {"page": "about"}
    return render(request, "home/about.html", context)


def contact(request):
    context = {"page": "contact"}
    return render(request, "home/contact.html", context)


def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Hey this is a Success page.</h1>")
