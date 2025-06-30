from django.shortcuts import render, redirect
from django.contrib import messages
from .models import GiPendente
import pandas as pd
from django.core.files.storage import FileSystemStorage

def gi_lista(request):
    # Lista todos os registros GI Pendente
    itens = GiPendente.objects.all()

    # Dados para gráfico: soma de quantidade por catálogo
    chart_labels = list(itens.values_list('catalogo', flat=True))
    chart_data = list(itens.values_list('quantidade', flat=True))

    return render(request, 'gi_pendente/gi_lista.html', {
        'itens': itens,
        'chart_labels': chart_labels,
        'chart_data': chart_data
    })

def gi_importar_excel(request):
    if request.method == "POST" and request.FILES.get('arquivo'):
        arquivo = request.FILES['arquivo']

        # Salva arquivo temporário
        fs = FileSystemStorage()
        filename = fs.save(arquivo.name, arquivo)
        file_path = fs.path(filename)

        try:
            df = pd.read_excel(file_path)

            # Limpa a tabela antes de importar novos dados (opcional, depende do seu uso)
            GiPendente.objects.all().delete()

            for _, row in df.iterrows():
                GiPendente.objects.create(
                    catalogo = str(row.get('Catalog', '') or ''),
                    bin = str(row.get('BIN', '') or ''),
                    material = str(row.get('Material', '') or ''),
                    descricao = str(row.get('Description', '') or ''),
                    quantidade = int(row.get('Qnty', 0) or 0),
                    onde_foi_usado = str(row.get('Onde foi usado', '') or ''),
                    ordem = str(row.get('Ordem', '') or ''),
                    data = row.get('Data', None),
                    unit = float(row.get('Unit', 0) or 0),
                    total = float(row.get('Total', 0) or 0),
                )
            messages.success(request, 'Dados importados com sucesso!')
        except Exception as e:
            messages.error(request, f'Erro ao importar: {e}')
        fs.delete(filename)
        return redirect('gi_lista')

    return render(request, 'gi_pendente/gi_importar_excel.html')

def gi_dashboard(request):
    # Você pode montar um dashboard real depois.
    return render(request, 'gi_pendente/gi_dashboard.html')
