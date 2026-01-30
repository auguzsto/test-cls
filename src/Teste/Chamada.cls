Class Teste.Chamada Extends %RegisteredObject
{

ClassMethod Executar() As %Status
{
    return $$$OK
}

/// Este novo recusro foi adicionado pela branch feat/projeto
/// Ele será sincronizado com o servidor, imediamente, por tanto
/// deve haver, até então, um servidor de desenvolvimento.
ClassMethod NovoRecurso() As %Status
{
   return $$$OK
}

ClassMethod MaisUmNovoRecurso() As %Status
{
    Set sc = $$$OK
    // do something
    Return sc
}

/// Description
ClassMethod TestandoCapturaNoCI() As %Status
{
    Set sc = $$$OK
    // do something
    Return sc
}

}
