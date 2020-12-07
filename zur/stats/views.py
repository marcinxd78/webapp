from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from ur.models import Tag


def graph(request):
    bug_all_total = Tag.many_do_it
    bug_posted_total = Tag.many_not_do_it()
    print(bug_all_total)
    print(bug_posted_total)
    result = Tag.objects.all().values( 'fix_dep__name_fix_cat').order_by('fix_dep').annotate(count=Count('fix_dep'))
    print(result)
    result2 = Tag.objects.all().values('machine').order_by('machine').annotate(count=Count('machine'))
    print(result2)
    result3 = Tag.objects.all().values('work_cat__name_work_cat').order_by('work_cat').annotate(count=Count('work_cat'))
    print(result3)
    return render(request, 'graph.html', {'bug_all_total': bug_all_total,
               'bug_posted_total': bug_posted_total, 'result': result, 'result2': result2, 'result3': result3,})

# def count_tag_dep(request):
#     result = Tag.objects.values('fix_dep').order_by('fix_dep').annotate(count=Count('number'))
#     print(result[0].count)
#
#     return render(request, 'graph.html', {'result': result, })