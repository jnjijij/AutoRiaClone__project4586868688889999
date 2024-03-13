from django.shortcuts import render, redirect, get_object_or_404
from models import Listing
from forms import ListingForm
from models import CarListing
from models import HttpResponseForbidden
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.seller = request.user
            listing.save()
            return redirect('listing_detail', pk=listing.pk)
    else:
        form = ListingForm()
    return render(request, 'create_listing.html', {'form': form})

def edit_listing(request, pk):
    listing = Listing.objects.get(pk=pk)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing_detail', pk=pk)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'edit_listing.html', {'form': form, 'listing': listing})

def listing_details(request, listing_id):
    listing = get_object_or_404(CarListing, pk=listing_id)
    if request.user.account_type == 'premium' and listing.seller == request.user:
        # Logic to calculate and display the view statistics and average prices
        context = {
            'listing': listing,
            'views': listing.views,
            'views_today': listing.views_today,
            'views_this_week': listing.views_this_week,
            'views_this_month': listing.views_this_month,
            'average_price_region': listing.average_price_region,
            'average_price_city': listing.average_price_city,
            'average_price_country': listing.average_price_country
        }
        return render(request, 'listing_details_premium.html', context)
    else:
        return HttpResponseForbidden("You do not have permission to view this listing's details")
