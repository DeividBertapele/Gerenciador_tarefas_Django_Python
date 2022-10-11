from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import AdicionarTarefa, EditarTarefaForm

# criando a lista de tarefas
def tarefas_list(request):
    tarefas_pendentes = Tarefa.objects.filter(status='pendente')
    if request.method == 'POST':
        form = AdicionarTarefa(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas_list')
    else:
        form = AdicionarTarefa()
    return render(request, 'tarefas_list.html', {'tarefas_pendentes':tarefas_pendentes, 'form':form})


# para concluir as tarefas
def concluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'concluído'
    tarefa.save()
    return redirect('tarefas_list')


# para excluir a tarefa
def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    return redirect('tarefas_list')


# para adiar as tarefas
def adiar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'adiado'
    tarefa.save()
    return redirect('tarefas_list')


# editar as tarefas
def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        form = EditarTarefaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            tarefa.descricao = cd['tarefa']
            tarefa.categoria = cd['categoria']
            tarefa.save()
            return redirect('tarefas_list')
    else:
        form = EditarTarefaForm(initial={'tarefa':tarefa.descricao, 'categoria':tarefa.categoria})
        return render(request, 'editar_tarefa.html', {'tarefa':tarefa, 'form':form})


# Se as tarefas foram concluidas
def tarefas_concluidas_list(request):
    tarefas_concluidas = Tarefa.objects.filter(status='concluído')
    return render(request, 'tarefas_concluidas.html', {'tarefas_concluidas':tarefas_concluidas})

# Para adiar a lista de tarefas
def tarefas_adiadas_list(request):
    tarefas_adiadas = Tarefa.objects.filter(status='adiado')
    return render(request, 'tarefas_adiadas.html', {'tarefas_adiadas':tarefas_adiadas})


# para mover as tarefas
def mover_para_tarefas(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'pendente'
    tarefa.save()
    return redirect('tarefas_list')