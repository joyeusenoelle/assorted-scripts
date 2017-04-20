class Array

  def mean
    l = self.size.to_f
    r = true
    self.each do |x|
      if !x.respond_to?(:/) then r = false end
    end
    return r ? self.inject(:+) / l : self.median
  end

   def median
     return nil if self.empty?
     array = self.sort
     m_pos = array.size / 2
   return array.size % 2 == 1 ? array[m_pos] : (array[m_pos].respond_to?(:/) ? array[m_pos-1..m_pos].mean : array[m_pos-1..m_pos])
  end

  def nmax(n)
    return self.sort.reverse[0...n]
  end

  def nmin(n)
    return self.sort[0...n]
  end

  def uniq?
    return self == self.uniq ? true : false
  end

  def modes
    histogram = self.inject(Hash.new(0)) { |h,n| h[n] += 1; h }
    modes = nil
    histogram.each_pair do |item, times|
      modes << item if modes && times == modes[0]
      modes = [times, item] if (!modes && times>1) or (modes && times>modes[0])
    end
    return modes ? modes[1..modes.size] : modes
  end

end
