from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from teacher.models import Teacher
from .forms import TeacherCreateForm

extra_hour = 40
value_extra_hour = 1.5
parafiscal_enterprise = 0.09
parafiscal_worker = 0.08
# 0.0833 mensual 0.01917040255
bonus = 0.01917040255
severance = 0.01917040255
severance_interest = 0.01
# 0.0417 mensual 0.00959670812
vacation = 0.00959670812

health = 0.04
pension = 0.04


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "teacher/index.html", context)


class ListTeacherView(View):
    def get(self, request, *args, **kwargs):
        all_teachers = Teacher.objects.values_list("id", "name")
        context = {
            "all_teachers": all_teachers,
        }
        return render(request, "teacher/list_teacher.html", context)


class CreateTeacherView(View):
    def get(self, request, *args, **kwargs):
        form = TeacherCreateForm()

        context = {"form": form}
        return render(request, "teacher/create_teacher.html", context)

    def post(self, request, *args, **kwargs):
        form = TeacherCreateForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                cc = form.cleaned_data.get("cc")
                name = form.cleaned_data.get("name")
                work_hour = form.cleaned_data.get("work_hour")
                value_work = form.cleaned_data.get("value_work")

                t, created = Teacher.objects.get_or_create(
                    cc=cc, name=name, work_hour=work_hour, value_work=value_work
                )
                t.save()
                return redirect("teacher:home")
        context = {'form': form}
        return render(request, "teacher/create_teacher.html", context)


class ShowInfo(View):
    def get(self, request, id_user, *args, **kwargs):
        user = get_object_or_404(Teacher, id=id_user)
        if user.work_hour <= extra_hour:
            gross_value = round(user.work_hour * user.value_work, 2)
        else:
            gross_value = round(extra_hour * user.value_work, 2)

        value_extras = round(
            Teacher.calculate_extras_hours(
                user.work_hour, user.value_work, extra_hour, value_extra_hour
            ),
            2,
        )
        value_parafiscal_enterprise = round(
            Teacher.calculate_parafiscal_enterprise(gross_value, value_extras, parafiscal_enterprise), 2
        )
        value_parafiscal_worker = round(
            Teacher.calculate_parafiscal_worker(gross_value, value_extras, parafiscal_worker), 2
        )
        value_bonus = round(Teacher.calculate_bonus(gross_value, bonus), 2)
        value_severance = round(Teacher.calculate_severance(gross_value, severance), 2)
        value_severance_interest = round(
            Teacher.calculate_severance_interest(value_severance, severance_interest), 2
        )
        value_vacation = round(Teacher.calculate_vacation(gross_value, vacation), 2)
        value_health = round(Teacher.calculate_health(gross_value, health), 2)
        value_pension = round(Teacher.calculate_pension(gross_value, pension), 2)

        total_salary = round(sum([gross_value, value_extras, value_bonus, value_severance, value_severance_interest,
                                  value_vacation]) - value_parafiscal_worker - value_health - value_pension, 2)

        context = {
            "user": get_object_or_404(Teacher, id=id_user),
            "gross": gross_value,
            "extras": value_extras,
            "parafiscal_enterprise": value_parafiscal_enterprise,
            "parafiscal_worker": value_parafiscal_worker,
            "bonus": value_bonus,
            "severance": value_severance,
            "severance_interest": value_severance_interest,
            "vacation": value_vacation,
            "health": value_health,
            "pension": value_pension,
            "salary": total_salary,
        }
        return render(request, "teacher/show_info.html", context)


class ShowAllTeachers(View):
    def get(self, requets, *args, **kwargs):
        total_users = []
        all_users = Teacher.objects.all()
        for user in all_users:
            if user.work_hour <= extra_hour:
                gross_value = round(user.work_hour * user.value_work, 2)
            else:
                gross_value = round(extra_hour * user.value_work, 2)

            value_extras = round(
                Teacher.calculate_extras_hours(
                    user.work_hour, user.value_work, extra_hour, value_extra_hour
                ),
                2,
            )
            value_parafiscal_enterprise = round(
                Teacher.calculate_parafiscal_enterprise(gross_value, value_extras, parafiscal_enterprise), 2
            )
            value_parafiscal_worker = round(
                Teacher.calculate_parafiscal_worker(gross_value, value_extras, parafiscal_worker), 2
            )
            value_bonus = round(Teacher.calculate_bonus(gross_value, bonus), 2)
            value_severance = round(Teacher.calculate_severance(gross_value, severance), 2)
            value_severance_interest = round(
                Teacher.calculate_severance_interest(value_severance, severance_interest), 2
            )
            value_vacation = round(Teacher.calculate_vacation(gross_value, vacation), 2)
            value_health = round(Teacher.calculate_health(gross_value, health), 2)
            value_pension = round(Teacher.calculate_pension(gross_value, pension), 2)

            total_salary = round(sum([gross_value, value_extras, value_bonus, value_severance, value_severance_interest,
                                      value_vacation]) - value_parafiscal_worker - value_health - value_pension, 2)

            total_users.append({
                "user": get_object_or_404(Teacher, id=user.id),
                "gross": gross_value,
                "extras": value_extras,
                "parafiscal_enterprise": value_parafiscal_enterprise,
                "parafiscal_worker": value_parafiscal_worker,
                "bonus": value_bonus,
                "severance": value_severance,
                "severance_interest": value_severance_interest,
                "vacation": value_vacation,
                "health": value_health,
                "pension": value_pension,
                "salary": total_salary,
            })
        context = {'total_users': total_users}
        return render(requets, "teacher/show_all.html", context)
